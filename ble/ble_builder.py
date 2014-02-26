#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2013, Stephen Finucane

# Author: Stephen Finucane <stephenfinucane@hotmail.com>

import collections
import serial
import constants
class BLEBuilder():
	"""
	A builder for command packets as defined by the the Texas Instruments 
	Bluetooth Low Energy Host-Controller-Interface (HCI).
	
	Based on python-xbee library by Paul Malmsten.
	"""
	#dictionaries	
	#opcodes for command packets
	opcodes = constants.opcodes
	#structure of command packets
	hci_cmds = constants.hci_cmds

	def __init__(self, ser=None):
		"""
		Initialises the class

		@param ser: The file like serial port to use
		@type ser: serial.Serial
		"""
		self.serial_port = ser

	def _build_command(self, cmd, **kwargs):
		"""
		Constructs a HCI command to the serial port for this BLE device 

		>>> _build_command("fe31", param_id="\x15")
		('\\x01\\x31\\xfe\\x01\\x15', OrderedDict([
		('type', ('\\x01', 'Command')), 
		('op_code', ('\\x31\\xfe', 'GAP_GetParam')), 
		('data_len', ('\\x01', '01')), 
		('param_id', ('\\x15', '15'))])
		)

		It will expect named arguments for all fields other than those 
		with a default value or length of 'None'.

		>>> _build_command("fe31")
		Traceback (most recent call last):
		File "<stdin>", line 1, in <module>
		File "C:\Python27\lib\site-packages\pyblehci\\ble_builder.py", line 168, \
in _build_command % (field_name, field_len))
		KeyError: "The data provided for 'param_id' was not 1 bytes long"
	
		Each field will be written out in the order they are defined in the 
		command definition.

		@param cmd: The command to be written
		@type cmd: hex

		@param kwargs: Any additional parameters
		@type kwargs: hex

		@return: A tuple containing the hex command string and a parsed version 
		of the string stored in a dictionary.
		"""
		packet_type = "\x01"
		op_code 	= cmd.decode('hex')[::-1]	#command code was human-readable
		data_len 	= "\x00"	#insert dummy value for length

		#check for matching command codes in dictionary and store the matching
		# packet format
		try:
			packet_structure = self.hci_cmds[cmd]
		except AttributeError:
			raise NotImplementedError("Command spec could not be found")

		packet_type_parsed 	= "Command"
		op_code_parsed 	= self.opcodes[cmd]
		data_len_parsed 	= "0"	#insert dummy value for length

		#command match found, hence start storing result
		built_packet = collections.OrderedDict()
		built_packet['type'] 		= (packet_type, packet_type_parsed)
		built_packet['op_code'] 	= (op_code, op_code_parsed)
		built_packet['data_len'] 	= (data_len, data_len_parsed)

		packet = ''
		packet += packet_type
		packet += op_code
		packet += data_len

		#build the packet in the order specified, by processing each 
		# required value as needed
		for field in packet_structure:
			field_name = field['name']
			field_len = field['len']
			#try to read this field's name from the function arguments dict
			try:
				field_data = kwargs[field_name]
			#data wasn't given
			except KeyError:
				#only a problem is the field has a specific length...
				if field_len is not None:
					#...or a default value
					default_value = field['default']
					if default_value:
						#if it has a default value, use it
						field_data = default_value
					else:
						#otherwise fail
						raise KeyError("The data provided for '%s' was not %d bytes long"
							% (field_name, field_len))
				#no specific length, hence ignore it
				else:
					field_data = None

			#ensure that the correct number of elements will be written
			if field_len and len(field_data) != field_len:
				raise ValueError("The data provided for '%s' was not %d bytes long"
					% (field_name, field_len))

			#add the data to the packet if it has been specified (otherwise the
			# parameter was of variable length and not given)
			if field_data:
				packet += field_data
				built_packet[field_name] = (field_data, field_data.encode('hex'))

		#finally, replace the dummy length value 
		#in the string
		length = hex(len(packet) - 4)	#get length of bytes after 4th (length)
		data_len = length[2:].zfill(2).decode('hex')	#change 0x2 -> \x02
		modified_packet = list(packet)
		modified_packet[3] = data_len
		packet = "".join(modified_packet)
		#and the dictionary
		data_len_parsed = data_len.encode('hex')
		built_packet['data_len'] = (data_len, data_len_parsed)

		return (packet, built_packet)

	def send(self, cmd, **kwargs):
		"""
		Constructs and write a HCI command to the serial port for this BLE device

		>>> send(cmd="fe31", param_id="\x15")
		01:31:FE:01:15	#<-- also writes this to serial port

		This method must be called with the named arguments in accordance 
		with the HCI specification. Arguments matching all field names 
		other than those in the reserved_names (like 'id' and 'order')
		should be given, unless they are of variable length (of 'None' in
		the specification. These are optional).

		>>> send(cmd="fe31")
		Traceback (most recent call last):
		File "<stdin>", line 1, in <module>
		File "C:\Python27\lib\site-packages\pyblehci\\ble_builder.py", line 168, \
in _build_command % (field_name, field_len))
		KeyError: "The data provided for 'param_id' was not 1 bytes long"
	
		Each field will be written out in the order they are defined in the 
		command definition.

		@param cmd: The command to be written
		@type cmd: hex

		@param kwargs: Any additional parameters
		@type kwargs: hex

		@return: A tuple containing the hex command string and a parsed version 
		of the string stored in a dictionary.
		"""
		packet, built_packet = self._build_command(cmd, **kwargs)
		self.serial_port.write(packet)
		return (packet, built_packet)