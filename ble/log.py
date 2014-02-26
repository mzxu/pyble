#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2014, Mingze

# Author: Mingze (mxu@microstrategy.com)
import logging, os


class Formatter:
    command = "%(asctime)s - %(name)s - {%(pathname)s:%(lineno)d} - %(levelname)s - %(message)s"
    event = "%(asctime)s - %(name)s - {%(pathname)s:%(lineno)d} - %(levelname)s - %(message)s"
    performance = "%(asctime)s - %(threadName)s - %(levelname)s - %(message)s"
    ble = "%(asctime)s - %(name)s - {%(pathname)s:%(lineno)d} - %(levelname)s - %(message)s"
    
class Output:
    Console = "Console"
    File = "File"
    
class Name:
    command = "command"
    event = "event"
    performance = "performance"
    ble = "ble"

class Logger:
    def __init__(self, name = 'default', loglevel = logging.INFO, output = Output.Console, formatter = Formatter.ble, path = None,filename =None):
    
        self.logger = logging.getLogger(name)
        self.logger.setLevel( loglevel )
        # create console handler and set level to debug
        if output == Output.File:
            if file is None or path is None:
                Exception("filename or path is missing!")
            logfile = os.path.join( path, filename )
            ch = logging.FileHandler(logfile)
        else:
            ch = logging.StreamHandler()
    
        # create formatter
        f = logging.Formatter(formatter)
        # add formatter to ch
        ch.setFormatter( f )
        # add ch to logger
        self.logger.addHandler( ch )
        self.logger.setLevel(loglevel)
    def get_logger(self):
        return self.logger
    

command = logging.getLogger() #for test scripts
event = logging.getLogger()
performance = logging.getLogger()
ble = logging.getLogger()






