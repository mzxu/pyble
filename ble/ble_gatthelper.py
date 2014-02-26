'''
Created on Jan 11, 2014

@author: mxu
This module does dirty work to handle gatt related request
'''

import sqlite3 as lite
import utils
import bluetooth


class sqls:
    sql_select_handles_in_range = '''
            select handle, value, properties, permission from defaultTable where uuid = "%s" and handle >= "%s" and handle < "%s";
            '''
    sql_select_primary_service_by_uuid = '''
            select handle from defaultTable where uuid = "%s" and value = "%s";
            '''
    sql_select_handles = '''
            select handle from defaultTable;
            '''
    sql_select_uuid_by_handle = '''
            select uuid from defaultTable where handle = "%s";
            '''
    
    sql_select_value_by_handle = '''
            select value, properties, permission from defaultTable where handle = "%s";
            '''

ATT_MTU = 20

class BLEGattHelper:
    '''
    classdocs
    '''
    

    def __init__(self,ble_builder):
        '''
        Constructor
        '''
        self.ble_builder = ble_builder
        self.handles = self._get_handles()
        
        self.preserved_handle_eom = "0013"
        
    
    def AttGrpTypeRspHandler(self, dictionary):
        '''
        lookup the gatt table and select specific attributes to return
        '''

        def _sendATTGrpTypeRsp(conn_handle, data, data_length):
            #         data = "\x14\x00\x17\x00\x9d\x28\xd9\x02\x6e\x8a\x5a\xa8\xe7\x41\x41\x38\xa0\xf2\x83\xdb"
            print(utils.printOutput(self.ble_builder.send("fd11", conn_handle = conn_handle, data_length = data_length, value = data)))
            
        def _get_pdu(data):
            eof = "\xff\xff\xff\xff"
            pdu = ""
            length = "\x06"
#             if data:
#                 try:
#                     
#                     for i in range(len(data)):
#                         if data[i][0] == "0014":
#                             pass
#                         temp_start = utils.stringToSByteInHex(data[i][0])[::-1]   #start handle
#                         temp_value = utils.stringToSByteInHex(data[i][1].replace(":",""))  #value     
#                         #get end handle            
#                         if i + 1 > range(len(data))[-1]:     
#                             temp_end = utils.stringToSByteInHex(self.handles[-1])[::-1]    #this is the last service, end handle is the last one of all handles
#                         else:
#                             temp_end = utils.stringToSByteInHex(utils.stringMinusInHex(data[i+1][0],1))[::-1]   #this is not the last service then the end handle is the handle of next service minus one
# 
# 
#                         if len(temp_value) == 16:     #this is 128bit uuid, then only return one service info
#                             pdu = temp_start + temp_end + temp_value  
#                             break    
#                         else:
#                             if len(pdu) + 4 + len(temp_value) > 12 :  #if total pdu exceeds the maxmium length, do not append, only two services returned each time
#                                 break
#                             else:
#                                 pdu = pdu + temp_start + temp_end + temp_value #append pdu
#                 except Exception, e:
#                     print e
#                     pdu = eof
#             else:
#                 pdu = eof
            if data:
                try:
                    
                    for i in range(len(data)):
                        if data[i][0] == "001b":
                            pass
                        temp_start = utils.stringToSByteInHex(data[i][0])[::-1]   #start handle
                        temp_value = utils.stringToSByteInHex(data[i][1].replace(":",""))  #value     
                        #get end handle            
                        if i + 1 > range(len(data))[-1]:     
                            temp_end = utils.stringToSByteInHex(self.handles[-1])[::-1]    #this is the last service, end handle is the last one of all handles
                        else:
                            temp_end = utils.stringToSByteInHex(utils.stringMinusInHex(data[i+1][0],1))[::-1]   #this is not the last service then the end handle is the handle of next service minus one
        
        
                        if len(temp_value) == 16:     #this is 128bit uuid, then only return one service info
                            pdu = temp_start + temp_end + temp_value  
                            length = "\x14"   #set lenght to fit 128bit uuid
                            break    
                        else:
                            if len(pdu) + 4 + len(temp_value) > ATT_MTU :  #if total pdu exceeds the maxmium length, do not append, only two services returned each time
                                break
                            elif i + 1 <= range(len(data))[-1]:   
                                next_value = utils.stringToSByteInHex(data[i+1][1].replace(":",""))                
                                if len(next_value) == 16:
                                    if pdu:
                                        pdu = pdu + temp_start + temp_end + temp_value
                                    else:
                                        pdu = temp_start + temp_end + temp_value
                                    break
                                else:
                                    pdu = pdu + temp_start + temp_end + temp_value
                            else:
                                pdu = pdu + temp_start + temp_end + temp_value #append pdu
                except Exception, e:
                    print e
                    pdu = eof
            else:
                pdu = eof            
            return pdu, length
        
        conn_handle = dictionary['conn_handle']
        start_handle = dictionary['start_handle']
        end_handle = dictionary['end_handle']
        group_type = dictionary['group_type']        
        
        conn_handle = conn_handle[0]
        uuid = group_type[1]
        start = start_handle[1]
        end = end_handle[1]
        sql = sqls.sql_select_handles_in_range % (uuid, start, end)
        data = self._execute_sql(sql)
        pdu = _get_pdu(data)
        
        _sendATTGrpTypeRsp(conn_handle, pdu[0], pdu[1])

        pass
    
    def ATTReadByTypeRspHandler(self, dictionary):
        '''
        Limitation: 
        1. cuurently only consider one key-value pair to return, it is becuase most of cases only one key should be found
        2. no permission restriction, all data are readable 
        '''
        def _sendATTReadByTypeRsp(conn_handle, value, data_length):
            print("COMMAND: ATT_ReadByTypeRsp")
            print(utils.printOutput(self.ble_builder.send("fd09", conn_handle = conn_handle, data_length = data_length, value = value)))

        def _get_pdu(data):
            handle = utils.stringToSByteInHex(data[0][0])[::-1]
            value = utils.stringToSByteInHex(data[0][1], ":")
            pdu = handle + value
            return pdu
        
        conn_handle = dictionary['conn_handle']
        start_handle = dictionary['start_handle']
        end_handle = dictionary['end_handle']
        _type = dictionary['type']           
        
        conn_handle = conn_handle[0]
        start = start_handle[1]
        end = end_handle[1]
        uuid = _type[1]
        #get data from gatt table
        sql = sqls.sql_select_handles_in_range % (uuid, start, end)
        data = self._execute_sql(sql) 
        pdu = _get_pdu(data)
        data_length = utils.getByteDataLengh(pdu)
        

        _sendATTReadByTypeRsp(conn_handle, pdu, data_length)     

    
    def ATTReadBlobRspHandler(self, dictionary):
        '''
        lookup value in gatt table for a given handle 
        '''
        def _sendATTReadBlobRsp(conn_handle, value):
            print("COMMAND: ATT_ReadBlobRsp")
            print(utils.printOutput(self.ble_builder.send("fd0d", conn_handle = conn_handle, value = value)))
        
        conn_handle = dictionary['conn_handle']
        handle = dictionary['handle']
        req_opcode = dictionary['event'][0]
                 
        conn_handle = conn_handle[0]
        handle_str = handle[1]
        handle_raw = utils.stringToSByteInHex(handle[1])
        #get data from gatt table
        sql = sqls.sql_select_value_by_handle % handle_str
        data = self._execute_sql(sql)  
        
        value = utils.stringToSByteInHex(data[0][0], ":")
        data_property = data[0][1]
        data_permission = data[0][2]
        if data_property:
            properties = utils.stringToSByteInHex(data_property)
        else:
            properties = None
        if data_permission:
            permission = utils.stringToSByteInHex(data_permission)
        else:
            permission = None
            
        if self._canRead(properties, permission):
            _sendATTReadBlobRsp(conn_handle, value)     
        else:
            self.ATTErrorRspHandler(conn_handle, req_opcode[-1], handle_raw, bluetooth.errorRsp.READ_NOT_PERMITTED)
    
    def ATTWriteReqHandler(self, dictionary, func):
        '''
        handle write req,
        Limitation: no signature and command type checking
        '''
        def _sendATTWriteRsp(conn_handle):
            print("COMMAND: ATT_WriteRsp")
            print(utils.printOutput(self.ble_builder.send("fd13", conn_handle = conn_handle)))
            
        def _handleIndication(conn_handle, handle, start_handle, end_handle): #to-do refactor for better usability
            print("COMMAND: ATT_HandleValueIndication")
            handle = handle
            value = start_handle+end_handle
#             print(utils.printOutput(self.ble_builder.send("fd1d", conn_handle = conn_handle, handle = handle, value = value)))
        
        conn_handle = dictionary['conn_handle'][0]
        handle = dictionary['handle']
        value = dictionary['value']
        value_str = value[1]
        handle_raw = handle[0]
        handle_str = handle[1]
        
        _sendATTWriteRsp(conn_handle)      
        #get data from gatt table

        if handle_str < self.preserved_handle_eom: #attampt to write preserved services
            if handle_str == "0009" and value_str == "0002": #ask for service changes, tempararily fix to return non-reserved handles
                start_handle = utils.stringToSByteInHex(utils.stringMinusInHex(self.preserved_handle_eom, -1))[::-1]
                end_handle = utils.stringToSByteInHex(self.handles[-1])[::-1]
                char_handle = utils.hexMinusInHex(handle_raw, 1)
                _handleIndication(conn_handle, char_handle, start_handle, end_handle)
        else:  #external services, tempararily fix to trigger call notification call back or do nothing
            if value_str == "0001": #Notification
                sql = sqls.sql_select_uuid_by_handle % utils.stringMinusInHex(handle_str, 1)
                data = self._execute_sql(sql)  
                uuid = data[0][0]
                char_handle = utils.hexMinusInHex(handle_raw, 1)
                func(uuid, char_handle, conn_handle)
            

     
    def ATTErrorRspHandler(self, conn_handle, req_opcode, handle, error_code):
        print("COMMAND: ATT_ErrorRsp")
        handle = handle
        print(utils.printOutput(self.ble_builder.send("fd01", conn_handle = conn_handle, req_opcode = req_opcode, handle = handle, error_code = error_code)))           
    
    def _get_handles(self):
        sql = sqls.sql_select_handles
        data = self._execute_sql(sql)
        handles = []
        for row in data:
            handles.append(row[0])        
        return handles

    def _canRead(self, properties, permission):
        '''
        Logic: 
        1. if permission is None and properties is Read, can Read
        2. if permission is readable or read/write, then if properties is None, can read
        3. if permission is readable or read/write, then if properties is Read, can read
        '''
        
        if not permission:
            if properties:
                if (properties[-1] == bluetooth.properties.Read):
                    return True
        
        if (permission == bluetooth.attrPermission.GATT_PERMIT_READ) \
            or (permission == bluetooth.attrPermission.GATT_PERMIT_READ_AND_WRITE):
            if not properties:
                return True
            if (properties[-1] == bluetooth.properties.Read):
                return True
        return False
                
    def _execute_sql(self, sql):
        try:
            data = []
            conn = lite.connect('gattServer.rdb')
            conn.text_factory = str
            cursor = conn.cursor()            
            cursor.execute(sql)
            if "select" in sql:
                for row in cursor:
                    data.append(row) 
            else:
                pass
            conn.commit()
                          
        except Exception, e:
            print e
                        
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()   
        return data 
    


        

def _get_pdu( data):
    eof = "\xff\xff\xff\xff"
    pdu = ""
    if data:
        try:
            
            for i in range(len(data)):
                if data[i][0] == "0014":
                    pass
                temp_start = utils.stringToSByteInHex(data[i][0])[::-1]   #start handle
                temp_value = utils.stringToSByteInHex(data[i][1].replace(":",""))  #value     
                #get end handle            
                if i + 1 > range(len(data))[-1]:     
                    temp_end = utils.stringToSByteInHex("001b")[::-1]    #this is the last service, end handle is the last one of all handles
                else:
                    temp_end = utils.stringToSByteInHex(utils.stringMinusInHex(data[i+1][0],1))[::-1]   #this is not the last service then the end handle is the handle of next service minus one


                if len(temp_value) == 16:     #this is 128bit uuid, then only return one service info
                    pdu = temp_start + temp_end + temp_value  
                    break    
                else:
                    if len(pdu) + 4 + len(temp_value) > 12 :  #if total pdu exceeds the maxmium length, do not append, only two services returned each time
                        break
                    elif i + 1 <= range(len(data))[-1]:   
                        next_value = utils.stringToSByteInHex(data[i+1][1].replace(":",""))                
                        if len(next_value) == 16:
                            if pdu:
                                pdu = pdu + temp_start + temp_end + temp_value
                                break
                            else:
                                pdu = temp_start + temp_end + temp_value
                                break
                        else:
                            pdu = pdu + temp_start + temp_end + temp_value
                    else:
                        pdu = pdu + temp_start + temp_end + temp_value #append pdu
        except Exception, e:
            print e
            pdu = eof
    else:
        pdu = eof
    return pdu.encode('hex')

        
if __name__ == '__main__':
    data = [("0001", "00:04")]
    print _get_pdu(data)
    data = [("0001", "00:00"), ("0004", "01:02")]
    print _get_pdu(data)
    data = [("0005", "00:00"), ("0008", "01:02"), ("000a", "02:02")]
    print _get_pdu(data)
    data = [("000d", "00:00"), ("001a", "01:02"), ("001f", "02:02"), ("0022", "03:04")]
    print _get_pdu(data)
    data = [("0001", "00:00"), ("0004", "01:02:03:04:05:06:07:08:09:10:11:12:13:14:15:16:"), ("0008", "02:02")]
    print _get_pdu(data)    
    data = [("0001", "00:00"), ("0003", "abef"), ("000a", "01:02:03:04:05:06:07:08:09:10:11:12:13:14:15:16:"), ("0008", "02:02")]
    print _get_pdu(data)    
    data = [("0001", "00:00"), ("0003", "abef"), ("0007", "dddd"), ("000a", "01:02:03:04:05:06:07:08:09:10:11:12:13:14:15:16:"), ("0008", "02:02")]
    print _get_pdu(data)    
    data = [("0004", "01:02:03:04:05:06:07:08:09:10:11:12:13:14:15:16:"),("0001", "00:00"),  ("0008", "02:02")]
    print _get_pdu(data)
    data = []
    print _get_pdu(data)