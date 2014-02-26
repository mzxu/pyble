'''
Created on Dec 19, 2013

@author: mxu
'''
import time,urllib2

from bluetooth import bluetooth


import re

charUUID = "\xD4\xC3"



    
def main():
    def DidDiscoverSuccess(devAddr, devRSSI, Data):
        print "Device: %s\t RSSI: %s\t Data: %s" % (devAddr[1], devRSSI, Data[1])
        if devRSSI > 200:
            b.DoConnect(devAddr[0])
#            OpenDoor()    
        

    def DidConnectSuccess(devAddr):
        print "Device: %s connected" % devAddr[1]
        
        b.DoReadUsingCharUUID(charUUID)
        
    def DidReadCharUsingUUIDSuccess(data):
        print "Char UUID: %s \t Data: %s" % (charUUID, data)

    
        
    def OpenDoor():

        urllib2.urlopen("https://uvs.usher.com/user/process_tag/TkhE6k4w0hcvB-w==:15064:25cfc71a46?%2Fuser%2Fprocess_tag%2FTugJVcNBa9hC3nQ=&uvs_access_token=tpwito5nsm4le6f0wesmn0jpfm0qq580kmj_MjI0MDgxZjA2OGM5ZmVmOTU0M2ZBNC1EMS1EMi04Qy00NS0zRA%3D%3D")
        print "open the door"
    while 1:          
        b = bluetooth(port = "COM6")
        b.register_callback(command = DidDiscoverSuccess)
        b.register_callback(command = DidConnectSuccess)
        b.register_callback(command = DidReadCharUsingUUIDSuccess)  

        b.DoDiscover()
        time.sleep(5)
        b.stop()
    #close device

    
if __name__ == "__main__":    
    main()

    #b = bluetooth(port = "COM5")
    #callback = PermanentCallback(DidDiscover)
    #b.RegisterCallback(callback)
    #b.DoDiscover()
    #sleep main thread for 15 seconds - allow results of device scan to return

    