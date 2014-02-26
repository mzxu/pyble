'''
Created on Jan 11, 2014

@author: mxu
'''
import sys
import collections
import base64

def getByteDataLengh(data):
    '''
    length shouldn't be larger than 255
    '''
    length = len(data.encode('hex'))/2
    if len(("%x" % length)) == 1:
        return ("0%x" % length).decode('hex')
    elif len(("%x" % length)) == 2:
        return ("%x" % length).decode('hex')
    else:
        raise Exception("length shouldn't be larger than 255!")
    
def processDevaddr(self, devAddr):
    addr_list = list(devAddr)
    addr = "" 
    for i in reversed(range(0, addr_list.__len__()-1, 2)):
        
        addr += r'\x'
        addr += addr_list[i]
        addr += addr_list[i+1]
        if i == 0:
            break

    return addr

def stringMinusInHex(s, num):
    '''
    "001a" - 1 = "0019"
    '''
    return format((int(s, 16)-num),'04x')
    
def hexMinusInHex(h, num):
    '''
    "\x1a\x00" -1 = "\x19\x00"
    '''
    s = h[::-1].encode('hex')
    s = stringMinusInHex(s, num)
    h = s.decode('hex')[::-1]
    return h

def stringToSByteInHex(s, split = None):
    '''
    split is None: "fe7a" -> "\xfe\x7a"
    split is ":" : "fe:7a" -> "\xfe\x7a"
    '''
    if not split:
        return base64.b16decode(s.upper())
    else:
        return base64.b16decode(s.replace(split, "").upper())

def hexToAscii(hex_data):
    string = ""
    for hex_value in hex_data:
        string += chr(int(hex_value.encode('hex'), 16))
    return string

def _pretty(hex_string, seperator=None):
    # >>> pretty("\x01\x02\x03\xff")
    #       '01 02 03 FF'
    if seperator: 
        sep = seperator 
    else: sep = ' '
    hex_string = hex_string.encode('hex')
    a = 0
    out = ''
    for i in range(len(hex_string)):
        if a == 2:
            out = out + sep
            a = 0
        out = out + hex_string[i].capitalize()
        a = a + 1
    return out

def _print_orderedDict(dictionary):
    result = ""
    for idx, key in enumerate(dictionary.keys()):
        if dictionary[key]:
            #convert e.g. "data_len" -> "Data Len"
            title = ' '.join(key.split("_")).title()
            if isinstance(dictionary[key], list):
                for idx2, item in enumerate(dictionary[key]):
                    result += "{0} ({1})\n".format(title, idx2)
                    result += _print_orderedDict(dictionary[key][idx2])
            elif isinstance(dictionary[key], type(collections.OrderedDict())):
                result += '{0}\n{1}'.format(title, _print_orderedDict(dictionary[key]))
            else:
                result += "{0:15}\t: {1}\n\t\t  ({2})\n".format(title, _pretty(dictionary[key][0], ':'), dictionary[key][1])
        else:
            result += "{0:15}\t: None".format(key)
    return result

def printOutput((packet, dictionary)):
    result = _print_orderedDict(dictionary)
    result += 'Dump:\n{0}\n'.format(_pretty(packet))
    return result