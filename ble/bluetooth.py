#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2013, Mingze

# Author: Mingze (mxu@microstrategy.com)


import sys
import collections
import serial
import time


from ble_builder import  BLEBuilder
from ble_parser import BLEParser
from ble_gatthelper import BLEGattHelper
from constants import event as hci_event
import utils

class Role:
    central =   "central"
    periphral = "peripheral"

class eventType:
    CONN_UNDIRECT_AD =      "\x00"
    CONN_DIRECT_AD =        "\x01"
    SCANABLE_UNDIRECT_AD =  "\x02"
    NON_CONN_UNDIRECT_AD =  "\x03"
    SCAN_RESPONSE =         "\x04"
    
class initiatorAddrType:
    Public =            "\x00"
    Static =            "\x01"
    PrivateNonResolve = "\x02"
    PrivateResolve =    "\x03"
    
class filterPolicy:
    All =       "\x00"
    WhiteScan = "\x01"
    WhiteCon =  "\x02"
    White =     "\x03"

class declarations:
    '''
    See https://developer.bluetooth.org/gatt/declarations/Pages/DeclarationsHome.aspx
    '''
    GATTPrimaryService =        "\x00\x28"
    GATTSecondaryService =      "\x01\x28"
    GATTInclude =               "\x02\x28"
    GATTCharacteristic =        "\x03\x28"

class descriptors:
    '''
    See https://developer.bluetooth.org/gatt/descriptors/Pages/DescriptorsHomePage.aspx
    '''    
    ClientCharacteristicConfiguration = '\x02\x29' #0x2902
    ServerCharacteristicConfiguration = '\x03\x29' #0x2903
    
class properties:
    Broadcasting =      "\x01"
    Read =              "\x02"
    WriteNoResponse =   "\x04"
    Write =             "\x08"
    Notify =            "\x10"
    Indicate =          "\x20"
    WriteSigned =       "\x40"    
    ExtendedProperty =  "\x80"

class attrPermission:
    GATT_PERMIT_READ =              "\x01"
    GATT_PERMIT_WRITE =             "\x02"
    GATT_PERMIT_READ_AND_WRITE =    "\x03"

class errorRsp:
    INVALID_HANDLE =            "\x01"
    READ_NOT_PERMITTED =        "\x02"
    WRITE_NOT_PERMITTED =       "\x03"
    INVALID_PDU =               "\x04"
    INSUFFICIENT_AUTHEN =       "\x05" 
    UNSUPPORTED_REQ =           "\x06"
    INVALID_OFFSET =            "\x07"
    INSUFFICIENT_AUTHOR =       "\x08"
    PREPARE_QUEUE_FULL =        "\x09"
    ATTR_NOT_FOUND =            "\x0a"
    ATTR_NOT_LONG =             "\x0b"
    INSUFFICIENT_KEY_SIZE =     "\x0c"
    INVALID_SIZE =              "\x0d"
    UNLIKELY_ERROR =            "\x0e"
    INSUFFICIENT_ENCRYPTION =   "\x0f"
    UNSUPPORTED_GRP_TYPE =      "\x10"
    INSUFFICIENT_RESOURCES =    "\x11"
    INVALID_VALUE =             "\x80"
    
class HostErrorCode:
    SUCCESS =                   "\x00"
    FAILURE =                   "\x01"
    INVALIDPARAMETER =          "\x02"
    INVALID_TASK =              "\x03"
    MSG_BUFFER_NOT_AVAIL =      "\x04"
    INVALID_MSG_POINTER =       "\x05"
    INVALID_EVENT_ID =          "\x06"
    INVALID_INTERRUPT_ID =      "\x07"
    NO_TIMER_AVAIL =            "\x08"
    NV_ITEM_UNINIT =            "\x09"
    NV_OPER_FAILED =            "\x0a"
    INVALID_MEM_SIZE =          "\x0b"
    NV_BAD_ITEM_LEN =           "\x0c"
    bleNotReady =               "\x10"
    bleAlreadyInRequestedMode = "\x11"
    bleIncorrectMode =          "\x12"
    bleMemAllocError =          "\x13"
    bleNotConnected =           "\x14"
    bleNoResources =            "\x15"
    blePending =                "\x16"
    bleTimeout =                "\x17"
    bleInvalidRange =           "\x18"
    bleLinkEncrypted =          "\x19"
    bleProcedureComplete =      "\x1a"
    bleGAPUserCanceled =        "\x30"
    bleGAPConnNotAcceptable =   "\x31"
    bleGAPBondRejected =        "\x32"
    bleInvalidPDU =             "\x40"
    
class disconnectReason:
    AUTHENTICATION_FAILURE =                "\x05"
    REMOTE_USER_TERMINATED =                "\x13"
    LOW_RESOURCES =                         "\x14"
    POWER_OFF =                             "\x15"
    UNSUPPORTED_REMOTE_FEATURE =            "\x1a"
    PAIRING_WITH_UNIT_KEY_NOT_SUPPORTED =   "\x29"
    UNACCEPTABLE_CONNECTION_INTERVAL =      "\x3b"
    
class linkTerminatedReason:
    SUPERVISOR_TIMEOUT              = "\x08"
    PEER_REQUESTED                  = "\x13"
    HOST_REQUESTED                  = "\x16"
    CONTROL_PACKET_TIMEOUT          = "\x22"
    CONTROL_PACKET_INSTANT_PASSED   = "\x28"
    LSTO_VIOLATION                  = "\x3b"
    MIC_FAILURE                     = "\x3d"

class resetType:
    HARD_RESET  = "\x00"
    SOFT_RESET  = "\x01"

class AdType:
    ADVERTISEMENT_DATA = "\x00"
    SCAN_RSP_DATA = "\x01"
    
rxServerMTU = "\x23\x00" #it's mtu value predefined by cc2540 chip, should be able to change but currently we'd better not do that.

class ble:

    def __init__(self, port = 'COM3'):
        
        
        self.port = port
        
        #init serial port
        self._init_serial_port()
        #init ble builder
        self.ble_builder = BLEBuilder(self.serial_port)
        #init ble parser
        self.ble_parser = BLEParser(self.serial_port, callback=self._display_packet)       
        #gatt server configuration
        self.gatt_server = BLEGattHelper(self.ble_builder)
        
       
        
        #init device
        time.sleep(1)
#         #get an operating parameter value
#         print("COMMAND: Getting operating parameter value")
#         print(print_output(self.ble_builder.send("fe31", param_id="\x15"))) 
    def _init_serial_port(self):
        print "Port is set to %s" % self.port
        self.serial_port = serial.Serial()
        self.serial_port.port = self.port
        self.serial_port.baudrate = 115200
        if self.serial_port.isOpen():
            self.serial_port.close()
        self.serial_port.open()
        
    def DoInitDevice(self, role = Role.central):
        self.role = role
        print("COMMAND: Initializing device as %s role" % self.role)
        if self.role == Role.central:
            print(utils.printOutput(self.ble_builder.send("fe00")))
        elif self.role == Role.periphral:
            #init device as peripheral mode
            print(utils.printOutput(self.ble_builder.send("fe00", profile_role = "\x04")))  
    
    def DoUpdateAdvertisingData(self, data, ad_type = AdType.ADVERTISEMENT_DATA):
        print("COMMAND: Set advertising data as %s " % data)
        data_length = utils.getByteDataLengh(data)
        print(utils.printOutput(self.ble_builder.send("fe07", advert_data = data, data_length = data_length, ad_type= ad_type)))        

    def DoMakeDiscoverable(self, event_type = eventType.NON_CONN_UNDIRECT_AD, init_addr_type = initiatorAddrType.PrivateResolve, filter_policy = filterPolicy.All):
        print("COMMAND: GAP_MakeDeviceDiscoverable")
        print(utils.printOutput(self.ble_builder.send("fe06", event_type = event_type, init_addr_type = init_addr_type, filter_policy = filter_policy)))
        
    def DoEndDiscoverable(self):
        print("COMMAND: GAPT_EndDiscoverable")
        print(utils.printOutput(self.ble_builder.send("fe08")))
        
    def DoAddService(self, service_type = declarations.GATTPrimaryService, number = 1):
        print("COMMAND: GATT_AddService")
        print(utils.printOutput(self.ble_builder.send("fdfc", uuid = service_type, numAttrs = number)))
    
    def DoDelService(self, handle):
        print("COMMAND: GATT_DelService")
        print(utils.printOutput((self.ble_builder.send("fdfd", handle))))

    def DoAddAttribute(self, uuid, permissions = attrPermission.GATT_PERMIT_READ_AND_WRITE):
        print("COMMAND: GATT_AddAttribute")
        print(utils.printOutput(self.ble_builder.send("fdfe", uuid = uuid, permissions = permissions)))
    
    def DoFindInfo(self, conn_handle = '\xfe\xff', start_handle = '\x01\x00', end_handle = '\xff\xff'):
        print("COMMAND: ATT_FindInfoReq")
        print(utils.printOutput(self.ble_builder.send("fd04", conn_handle = conn_handle, start_handle = start_handle, end_handle = end_handle)))
        
    def DoSendNotification(self, conn_handle, handle, value):
        print("COMMAND: ATT_HandleValueNotification")
        print(utils.printOutput(self.ble_builder.send("fd1b", conn_handle = conn_handle, handle = handle, value = value)))
        
    def stop(self):
        self.ble_parser.stop()       
    
#     def DoHCIReset(self):
#         print("COMMAND: HCI reset")
#         print(utils.printOutput(self.ble_builder.send("0c03")))
        
        
    def DoDiscover(self):
        #start a device discovery scan
        print("COMMAND: Starting device scan")
#        print(utils.printOutput(self.ble_builder.send("fe05")))
#        time.sleep(0.1)
        print(utils.printOutput(self.ble_builder.send("fe04", mode="\x03")))
        
    def DoCancelDiscover(self):
        print("COMMAND: GAP_DeviceDiscoveryRequest")        
        print(utils.printOutput(self.ble_builder.send("fe05")))        

    def DoConnect(self, devAddr):
        print("COMMAND: Starting establishing connection to %s" % devAddr)
        print(utils.printOutput(self.ble_builder.send("fe05")))
        time.sleep(0.1)
#         print(utils.printOutput(self.ble_builder.send("fe0a", mode="\xFE\xFF")))
        time.sleep(0.1)
        print("COMMAND: GAP_EstablishLinkRequest")
        print(utils.printOutput(self.ble_builder.send("fe09", peer_addr=devAddr, addr_type_peer="\x03")))
    
    def DoReset(self, resetType):
        print("COMMAND: UTIL_Reset")
        print(utils.printOutput(self.ble_builder.send("fe80", resetType = resetType)))
        time.sleep(1)
    
    def DoDisconnect(self, conn_handle):
        print("COMMAND: GAP_TerminateLinkRequest")
        print(utils.printOutput(self.ble_builder.send("fe0a", conn_handle = conn_handle[0])))
        time.sleep(1)
        
    def DoFindPrimaryServices(self):
        pass
    
    def DoFindPrimaryServiceByUUID(self, serviceUUID, conn_handle):
        print("COMMAND: GATT_DiscPrimaryServiceByUUID")
        print(utils.printOutput(self.ble_builder.send("fd86", value = serviceUUID, conn_handle = conn_handle[0])))        
        pass
    
    def DoDiscCharsByUUID(self, charUUID, start_handle, end_handle, conn_handle):
        print("COMMAND: GATT_DiscCharsByUUID")
        print(utils.printOutput(self.ble_builder.send("fd88", conn_handle = conn_handle[0], start_handle = start_handle[0], end_handle = end_handle[0], type=charUUID)))
    

    def DoEnableNotification(self, conf_handle, conn_handle):
        print("COMMAND: GATT_WriteCharValue")
        value = "\x01\x00"
        print(utils.printOutput(self.ble_builder.send("fd92", handle = conf_handle, value = value, conn_handle = conn_handle)))
    
    def DoReadUsingCharUUID(self, charUUID):
        print("COMMAND: Starting establishing connection")
        print(utils.printOutput(self.ble_builder.send("fdb4", read_type=charUUID)))
                

                
    def register_callback(self, command = None):
        print "register callback"
#        self._callback = command
        setattr(self, command.func_name, command)    
        
    def _DoExchangeMTURsp(self,conn_handle, rxServerMTU):
        print("COMMAND: ATT_ExchangeMTURsp")
        print(utils.printOutput(self.ble_builder.send("fd03",conn_handle = conn_handle, server_rx_mtu = rxServerMTU)))    
    
    def _DoCancelPendingConnectionRequest(self):
        print("COMMAND: Cancel pending connection request")
        print(utils.printOutput(self.ble_builder.send("fe0a", conn_handle="\xFE\xFF")))
    
    def _display_packet(self, (packet, dictionary)):
        print("EVENT: Response received from the device")
        print(utils.printOutput((packet, dictionary)))   
        event = dictionary['event'][1]
        status = dictionary['status'][1]
#         op_code = dictionary['op_code'][1]
        if event == hci_event.GAP_DeviceInformation:
            if hasattr(self, "DidDiscoverSuccess"):
                Data = dictionary['data_field']
                RSSI = int(dictionary['rssi'][1], 16)
                Addr = dictionary['addr']
                AddrType = dictionary['addr_type']
                func = getattr(self, "DidDiscoverSuccess") 
                func(Addr, RSSI, Data, AddrType)
        if event == hci_event.GAP_LinkEstablished:
            if hasattr(self, "DidConnectSuccess"):
                Addr = dictionary['dev_addr']
                ConnHandle = dictionary['conn_handle']
                func = getattr(self, "DidConnectSuccess")
                func(Addr, ConnHandle)
                
        #resp handler, mainly used in central mode        
        if event == hci_event.ATT_ErrorRsp:
            print "Error found!"

        if event == hci_event.ATT_FindByTypeValueRsp:
            if status == "00" and hasattr(self, "DidDiscPrimaryServiceByUUIDSuccess"):
                start_handle = dictionary['start_handle']
                end_handle = dictionary['end_handle']
                ConnHandle = dictionary['conn_handle']
                time.sleep(0.5)
                func = getattr(self, "DidDiscPrimaryServiceByUUIDSuccess")
                func(start_handle, end_handle, ConnHandle)
            
        if event == hci_event.ATT_ReadByTypeRsp:
            if dictionary.has_key('handle') and dictionary.has_key('value'):
                ConnHandle = dictionary['conn_handle']
                handle = dictionary['handle'][0]#dictionary['results']
                data = dictionary['value'][0]
                if len(data) > 3 and utils.hexMinusInHex(handle, -1) == data[1:3]:
                    #It's DiscUsingCharUUID event
                    charType = data[0]
                    charHandle = data[1:3]
                    confHandle = None
                    value = data[3::]
                    if charType.encode('hex')[0] == "1": #type is notify
                        confHandle = utils.hexMinusInHex(handle, -2)        
                    if hasattr(self, "DidDiscCharByUUIDSuccess"):     
                        time.sleep(0.5)       
                        func = getattr(self, "DidDiscCharByUUIDSuccess")
                        func(charType.encode('hex'), charHandle, confHandle, value, ConnHandle[0])     
                else:
                    #It's ReadUsingCharUUID event             
                    if hasattr(self, "DidReadCharByUUIDSuccess"):            
                        func = getattr(self, "DidReadCharByUUIDSuccess")
                        func(handle, data, ConnHandle)                    
            else:
                pass

        if event == hci_event.ATT_ReadByGrpTypeRsp:
            pass
        
        if event == hci_event.ATT_HandleValueNotification:
            conn_handle = dictionary['conn_handle']
            handle = dictionary['handle']
            value = utils.hexToAscii(dictionary['values'][0])
            if hasattr(self, "DidReciNotification"):
                func = getattr(self, "DidReciNotification")
                func(value, handle, conn_handle)
        if event == hci_event.ATT_HandleValueConfirmation:
            pass
        
        #Request handler mainly used in peripheral mode
        if event == hci_event.ATT_ReadByTypeReq:         
            self.gatt_server.ATTReadByTypeRspHandler(dictionary) 
            
        if event == hci_event.ATT_WriteReq:
            #if a write req recievied, it's probably to enable a notification or a indication
            #so pass the call back func to gatt helper in case a callback is needed.
            if hasattr(self, "DidRequestNotificationByCharUUID"):
                func = getattr(self, "DidRequestNotificationByCharUUID")
            else:
                func = None
            self.gatt_server.ATTWriteReqHandler(dictionary, func)
            
        if event == hci_event.ATT_ReadByGrpTypeReq:    
            self.gatt_server.AttGrpTypeRspHandler(dictionary)     
                   

        
        if event == hci_event.ATT_ReadBlobReq:

            self.gatt_server.ATTReadBlobRspHandler(dictionary)
            
        if event == hci_event.ATT_ExchangeMTUReq:
            conn_handle = dictionary['conn_handle'][0]
            self._DoExchangeMTURsp(conn_handle, rxServerMTU)  
            
                
        if event == hci_event.GAP_DeviceDiscoveryDone:            
            pass
        

        if event == hci_event.GAP_LinkTerminated:
            pass
        

        
        if event == hci_event.GAP_HCI_ExtensionCommandStatus:
            op_code = dictionary['op_code'][1]
            status = dictionary['status'][1]
            if op_code == "GAP_EstablishLinkRequest":
                if status == "11":   #cancel pending establish link request
                    self._DoCancelPendingConnectionRequest()
                

        
