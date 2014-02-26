#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2014, Mingze

# Author: Mingze (mxu@microstrategy.com)

class cmd:
    ATT_ErrorRsp                   = 'ATT_ErrorRsp',
    ATT_ExchangeMTUReq             = 'ATT_ExchangeMTUReq',
    ATT_ExchangeMTURsp             = 'ATT_ExchangeMTURsp',
    ATT_FindInfoReq                = 'ATT_FindInfoReq',
    ATT_FindInfoRsp                = 'ATT_FindInfoRsp',
    ATT_FindByTypeValueReq         = 'ATT_FindByTypeValueReq',
    ATT_FindByTypeValueRsp         = 'ATT_FindByTypeValueRsp',
    ATT_FindByTypeReq              = 'ATT_FindByTypeReq',
    ATT_FindByTypeRsp              = 'ATT_FindByTypeRsp',
    ATT_ReadReq                    = 'ATT_ReadReq',
    ATT_ReadRsp                    = 'ATT_ReadRsp',
    ATT_ReadBlobReq                = 'ATT_ReadBlobReq',
    ATT_ReadBlobRsp                = 'ATT_ReadBlobRsp',
    ATT_ReadByGrpTypeReq           = 'ATT_ReadByGrpTypeReq',
    ATT_ReadByGrpTypeRsp           = 'ATT_ReadByGrpTypeRsp',
    ATT_WriteReq                   = 'ATT_WriteReq',
    ATT_WriteRsp                   = 'ATT_WriteRsp',
    ATT_PrepareWriteReq            = 'ATT_PrepareWriteReq',
    ATT_PrepareWriteRsp            = 'ATT_PrepareWriteRsp',
    ATT_ExecuteWriteReq            = 'ATT_ExecuteWriteReq',
    ATT_ExecuteWriteRsp            = 'ATT_ExecuteWriteRsp',
    ATT_HandleValueNotification    = 'ATT_HandleValueNotification',
    ATT_HandleValueIndication      = 'ATT_HandleValueIndication',
    ATT_HandleValueConfirmation    = 'ATT_HandleValueConfirmation',
    GATT_DiscPrimaryServiceByUUID  = 'GATT_DiscPrimaryServiceByUUID',
    GATT_DiscCharsByUUID           = 'GATT_DiscCharsByUUID',
    GATT_ReadCharValue             = 'GATT_ReadCharValue',
    GATT_WriteCharValue            = 'GATT_WriteCharValue',
    GATT_ReadMultipleCharValues    = 'GATT_ReadMultipleCharValues',
    GATT_ReadMultipleCharValues    = 'GATT_WriteCharValue',
    GATT_WriteLongCharValue        = 'GATT_WriteLongCharValue',
    GATT_DiscAllChars              = 'GATT_DiscAllChars',
    GATT_ReadUsingCharUUID         = 'GATT_ReadUsingCharUUID',
    GATT_AddService                = 'GATT_AddService',
    GATT_DelService                = 'GATT_DelService',
    GATT_AddAttribute              = 'GATT_AddAttribute',
    GAP_DeviceInit                 = 'GAP_DeviceInit',
    GAP_ConfigureDeviceAddr        = 'GAP_ConfigureDeviceAddr',
    GATT_DeviceDiscoveryRequest    = 'GATT_DeviceDiscoveryRequest',
    GATT_DeviceDiscoveryCancel     = 'GATT_DeviceDiscoveryCancel',
    GAP_MakeDiscoverable           = 'GAP_MakeDiscoverable',
    GAP_UpdateAdvertisingData      = 'GAP_UpdateAdvertisingData',
    GAP_EndDiscoverable            = 'GAP_EndDiscoverable',
    GAP_EstablishLinkRequest       = 'GAP_EstablishLinkRequest',
    GAP_TerminateLinkRequest       = 'GAP_TerminateLinkRequest',
    GAP_UpdateLinkParamReq         = 'GAP_UpdateLinkParamReq',
    GAP_SetParam                   = 'GAP_SetParam',
    GAP_GetParam                   = 'GAP_GetParam',
    HTIL_Reset                     = 'HTIL_Reset'
    
class event:
    HCI_LE_ExtEvent                = 'HCI_LE_ExtEvent'
    ATT_ErrorRsp                   = 'ATT_ErrorRsp',
    ATT_ExchangeMTUReq             = 'ATT_ExchangeMTUReq',
    ATT_ExchangeMTURsp             = 'ATT_ExchangeMTURsp',
    ATT_FindInfoReq                = 'ATT_FindInfoReq',
    ATT_FindInfoRsp                = 'ATT_FindInfoRsp',
    ATT_FindByTypeValueReq         = 'ATT_FindByTypeValueReq',
    ATT_FindByTypeValueRsp         = 'ATT_FindByTypeValueRsp',
    ATT_ReadByTypeReq              = 'ATT_ReadByTypeReq',
    ATT_ReadByTypeRsp              = 'ATT_ReadByTypeRsp',
    ATT_ReadReq                    = 'ATT_ReadReq',
    ATT_ReadRsp                    = 'ATT_ReadRsp',
    ATT_ReadBlobReq                = 'ATT_ReadBlobReq',
    ATT_ReadBlobRsp                = 'ATT_ReadBlobRsp',
    ATT_ReadMultiReq               = 'ATT_ReadMultiReq',
    ATT_ReadMultiRsp               = 'ATT_ReadMultiRsp',
    ATT_ReadByGrpTypeReq           = 'ATT_ReadByGrpTypeReq',
    ATT_ReadByGrpTypeRsp           = 'ATT_ReadByGrpTypeRsp',
    ATT_WriteReq                   = 'ATT_WriteReq',
    ATT_WriteRsp                   = 'ATT_WriteRsp',
    ATT_PrepareWriteReq            = 'ATT_PrepareWriteReq',
    ATT_PrepareWriteRsp            = 'ATT_PrepareWriteRsp',
    ATT_ExecuteWriteReq            = 'ATT_ExecuteWriteReq',
    ATT_ExecuteWriteRsp            = 'ATT_ExecuteWriteRsp',
    ATT_HandleValueNotification    = 'ATT_HandleValueNotification',
    ATT_HandleValueIndication      = 'ATT_HandleValueIndication',
    ATT_HandleValueConfirmation    = 'ATT_HandleValueConfirmation',
    GATT_ClientCharCfgUpdated      = 'GATT_ClientCharCfgUpdated', 
    GATT_DiscCharsByUUID           = 'GATT_DiscCharsByUUID',
    GAP_DeviceInitDone             = 'GAP_DeviceInitDone',
    GAP_DeviceDiscoveryDone        = 'GAP_DeviceDiscoveryDone',
    GAP_AdvertDataUpdateDone       = 'GAP_AdvertDataUpdateDone',
    GAP_MakeDiscoverableDone       = 'GAP_MakeDiscoverableDone',
    GAP_EndDiscoverableDone        = 'GAP_EndDiscoverableDone',
    GAP_LinkEstablished            = 'GAP_LinkEstablished',
    GAP_LinkTerminated             = 'GAP_LinkTerminated',
    GAP_LinkParamUpdate            = 'GAP_LinkParamUpdate',
    GAP_DeviceInformation          = 'GAP_DeviceInformation',
    GAP_HCI_ExtensionCommandStatus = 'GAP_HCI_ExtensionCommandStatus',


            

opcodes =   {
             "fd01":cmd.ATT_ErrorRsp,
             "fd02":cmd.ATT_ExchangeMTUReq,
             "fd03":cmd.ATT_ExchangeMTURsp,
             "fd04":cmd.ATT_FindInfoReq,
             "fd05":cmd.ATT_FindInfoRsp,
             "fd06":cmd.ATT_FindByTypeValueReq,
             "fd07":cmd.ATT_FindByTypeValueRsp,
             "fd08":cmd.ATT_FindByTypeReq,
             "fd09":cmd.ATT_FindByTypeRsp,
             "fd0a":cmd.ATT_ReadReq,
             "fd0b":cmd.ATT_ReadRsp,
             "fd0c":cmd.ATT_ReadBlobReq,
             "fd0d":cmd.ATT_ReadBlobRsp,
             "fd10":cmd.ATT_ReadByGrpTypeReq,
             "fd11":cmd.ATT_ReadByGrpTypeRsp,
             "fd12":cmd.ATT_WriteReq,
             "fd13":cmd.ATT_WriteRsp,
             "fd16":cmd.ATT_PrepareWriteReq,
             "fd17":cmd.ATT_PrepareWriteRsp,
             "fd18":cmd.ATT_ExecuteWriteReq,
             "fd19":cmd.ATT_ExecuteWriteRsp,
             "fd1b":cmd.ATT_HandleValueNotification,
             "fd1d":cmd.ATT_HandleValueIndication,
             "fd1e":cmd.ATT_HandleValueConfirmation,
             "fd86":cmd.GATT_DiscPrimaryServiceByUUID,
             "fd88":cmd.GATT_DiscCharsByUUID,
             "fd8a":cmd.GATT_ReadCharValue,
             "fd8e":cmd.GATT_ReadMultipleCharValues,
             "fd92":cmd.GATT_WriteCharValue,
             "fd96":cmd.GATT_WriteLongCharValue,
             "fdb2":cmd.GATT_DiscAllChars,
             "fdb4":cmd.GATT_ReadUsingCharUUID,
             "fdfc":cmd.GATT_AddService,
             "fdfd":cmd.GATT_DelService,
             "fdfe":cmd.GATT_AddAttribute,
             "fe00":cmd.GAP_DeviceInit,
             "fe03":cmd.GAP_ConfigureDeviceAddr,
             "fe04":cmd.GATT_DeviceDiscoveryRequest,
             "fe05":cmd.GATT_DeviceDiscoveryCancel,
             "fe06":cmd.GAP_MakeDiscoverable,
             "fe07":cmd.GAP_UpdateAdvertisingData,
             "fe08":cmd.GAP_EndDiscoverable,
             "fe09":cmd.GAP_EstablishLinkRequest,
             "fe0a":cmd.GAP_TerminateLinkRequest,
             "fe11":cmd.GAP_UpdateLinkParamReq,
             "fe30":cmd.GAP_SetParam,
             "fe31":cmd.GAP_GetParam,
             "fe80":cmd.HTIL_Reset,
            }

hci_cmds =     {
            "fd01":
                [{'name':'conn_handle', 'len':2,    'default':'\x00\x00'},
                 {'name':'req_opcode',  'len':1,     'default':'\x00'},
                 {'name':'handle',        'len':2,    'default':'\x00\x00'},
                 {'name':'error_code',    'len':1,    'default':'\x00'}],
            "fd02":
                [{'name':'conn_handle', 'len':2,    'default':'\x00\x00'},
                 {'name':'client_rx_mtu','len':2,     'default':'\x00\x87'}],
            "fd03":
                [{'name':'conn_handle', 'len':2,    'default':'\x00\x00'},
                 {'name':'server_rx_mtu','len':2,     'default':'\x00\x87'}],
            "fd04":
                [{'name':'conn_handle', 'len':2,    'default':'\xff\xfe'},
                 {'name':'start_handle','len':2,    'default':'\x00\x01'},
                 {'name':'end_handle',    'len':2,    'default':'\xff\xff'}],
            "fd09":
                [{'name':'conn_handle', 'len':2,     'default':'\x00\x00'},
                 {'name':'data_length', 'len':1,    'default':None},
                 {'name':'value',        'len':None, 'default':None}],
            "fd0c":
                [{'name':'conn_handle', 'len':2,    'default':'\x00\x00'},
                 {'name':'handle',        'len':2,     'default':'\x00\x00'},
                 {'name':'offset',        'len':2,     'default':'\x00\x00'}],                
            "fd0d":
                [{'name':'conn_handle', 'len':2,    'default':'\x00\x00'},
                 {'name':'value',        'len':None, 'default':None}],
            "fd10":
                [{'name':'conn_handle', 'len':2,    'default':'\xff\xfe'},
                 {'name':'start_handle','len':2,    'default':'\x00\x01'},
                 {'name':'end_handle',    'len':2,    'default':'\xff\xff'},
                 {'name':'group_type',  'len':None, 'default':'\x00\x28'}], #by default it's service
            "fd11":
                [{'name':'conn_handle', 'len':2,    'default':'\x00\x00'},
                 {'name':'data_length', 'len':1,    'default':None},
                 {'name':'value',        'len':None, 'default':'\x00\x00'}],
            "fd13":
                [{'name':'conn_handle', 'len':2,    'default':'\x00\x00'}],
            "fd1b":
                [{'name':'conn_handle', 'len':2,    'default':'\x00\x00'},
                 {'name':'authenticated', 'len':1,  'default':'\x00'},
                 {'name':'handle',      'len':2,    'default':'\xfe\xff'},
                 {'name':'value',       'len':None, 'default':None}],
            "fd1d":
                [{'name':'conn_handle', 'len':2,    'default':'\x00\x00'},
                 {'name':'authenticated', 'len':1,  'default':'\x00'},
                 {'name':'handle',      'len':2,    'default':'\xfe\xff'},
                 {'name':'value',       'len':None, 'default':None}],
            "fd1e":
                [{'name':'conn_handle', 'len':2,    'default':'\x00\x00'}],
            "fd86":
                [{'name':'conn_handle',    'len':2,    'default':'\x00\x00'},
                 {'name':'value',        'len':None, 'default':None}],
            "fd88":
                [{'name':'conn_handle', 'len':2,    'default':'\x00\x00'},
                 {'name':'start_handle','len':2,    'default':'\x01\x00'},
                 {'name':'end_handle',    'len':2,    'default':'\xfe\xff'},
                 {'name':'type',        'len':None, 'default':None}],
            "fd8a":
                [{'name':'conn_handle',    'len':2,    'default':'\x00\x00'},
                 {'name':'handle',        'len':2,    'default':None}],
            "fd8c":
                [{'name':'conn_handle', 'len':2,    'default':'\x00\x00'},
                 {'name':'handle',        'len':2,     'default':'\x00\x00'},
                 {'name':'offset',        'len':2,     'default':'\x00\x00'},
                 {'name':'type',        'len':1,    'default':'\x00'}],
            "fd8e":
                [{'name':'conn_handle',    'len':2,    'default':'\x00\x00'},
                 {'name':'handles',        'len':None,    'default':None}],
            "fd92":
                [{'name':'conn_handle',    'len':2,    'default':'\x00\x00'},
                 {'name':'handle',        'len':2,    'default':None},
                 {'name':'value',        'len':None,    'default':None}],
            "fd96":
                [{'name':'handle',        'len':2,    'default':'\x00\x00'},
                 {'name':'offset',        'len':1,    'default':None},
                 {'name':'value',        'len':None,    'default':None}],
            "fdb2":
                [{'name':'start_handle','len':2,    'default':'\x00\x00'},
                 {'name':'end_handle',    'len':2,    'default':'\xff\xff'}],
            "fdb4":
                [{'name':'conn_handle',    'len':2,    'default':'\x00\x00'},
                 {'name':'start_handle','len':2,    'default':'\x01\x00'},
                 {'name':'end_handle',    'len':2,    'default':'\xff\xff'},
                 {'name':'read_type',    'len':2,    'default':None}],
            "fdfc":
                [{'name':'uuid',         'len':2,    'default':'\x28\x00'},
                 {'name':'numAttrs',    'len':2,    'default':'\x00\x01'}],
            "fdfd":
                [{'name':'handle',        'len':2,     'default':'\x00\x01'}],
            "fdfe":
                [{'name':'uuid',        'len':None, 'default':'\x00\0x00'},
                 {'name':'permissions', 'len':1,    'default':'\x03'}],
            "fe00":
                [{'name':'profile_role','len':1,    'default':'\x08'},
                 {'name':'max_scan_rsps','len':1,    'default':'\xa0'},
                 {'name':'irk',            'len':16,    'default':'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'},
                 {'name':'csrk',        'len':16,    'default':'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'},
                 {'name':'sign_counter','len':4,    'default':'\x01\x00\x00\x00'}],
            "fe03":
                [{'name':'addr_type',    'len':1,    'default':None},
                 {'name':'addr',        'len':6,    'default':None}],
            "fe04":
                [{'name':'mode',        'len':1,    'default':None},
                 {'name':'active_scan',    'len':1,    'default':'\x01'},
                 {'name':'white_list',    'len':1,    'default':'\x00'}],
            "fe05":
                [],
            "fe06":
                [{'name':'event_type',  'len':1,    'default':'\x00'},
                 {'name':'init_addr_type', 'len':1, 'default':'\x00'},
                 {'name':'init_addrs',  'len':6,    'default':'\x00\x00\x00\x00\x00\x00'},
                 {'name':'channel_map', 'len':1,    'default':'\x07'},
                 {'name':'filter_policy','len':1,   'default':'\x00'}],
            "fe07":
                [{'name':'ad_type',     'len':1,    'default':'\x01'},
                 {'name':'data_length', 'len':1,    'default':None},
                 {'name':'advert_data', 'len':None, 'default':'\x02\x01\x07'}],
            "fe08":
                [],
            "fe09":
                [{'name':'high_duty_cycle','len':1,    'default':'\x00'},
                 {'name':'white_list',    'len':1,    'default':'\x00'},
                 {'name':'addr_type_peer','len':1,    'default':'\x00'},
                 {'name':'peer_addr',    'len':6,    'default':None}],
            "fe0a":
                [{'name':'conn_handle',    'len':2,    'default':'\x00\x00'},
                 {'name':'disconnect_reason', 'len':1, 'default':'\x13'}],
            "fe30":
                 [{'name':'param_id',    'len':1,    'default':None},
                  {'name':'param_value',    'len':2,    'default':None}],
            "fe31":
                 [{'name':'param_id',    'len':1,    'default':None}],
            "fe80":
                [{'name':'reset_type',    'len':1,    'default':'\x01'}],
            "0c03":
                [],
            }

hci_events = {"ff":
                {'name':event.HCI_LE_ExtEvent,
                  'structure':
                    [{'name':'ext_event',    'len':None}]},
            }

ext_events= {"0501":
                {'name':event.ATT_ErrorRsp,
                 'structure':
                     [{'name':'conn_handle',    'len':2},
                      {'name':'pdu_len',        'len':1},
                      {'name':'req_op_code',    'len':1},
                      {'name':'handle',        'len':2},
                      {'name':'error_code',    'len':1}]},
            "0502":
                {'name':event.ATT_ExchangeMTUReq,
                 'structure':
                      [{'name':'conn_handle', 'len':2},
                     {'name':'pdu_len',        'len':1},
                     {'name':'client_rx_mtu','len':2}]},
            "0503":
                {'name':event.ATT_ExchangeMTURsp,
                 'structure':
                      [{'name':'conn_handle', 'len':2},
                     {'name':'pdu_len',        'len':1},
                     {'name':'server_rx_mtu','len':2}]},
            "0504":
                {'name':event.ATT_FindInfoReq,
                 'structure':
                     [{'name':'conn_handle',    'len':2},
                     {'name':'pdu_len',        'len':1},
                     {'name':'start_handle','len':2},
                     {'name':'end_handle',    'len':2}]},
            "0505":
                {'name':event.ATT_FindInfoRsp,
                 'structure':
                     [{'name':'conn_handle', 'len':2},
                     {'name':'pdu_len',        'len':1},
                     {'name':'format',        'len':1},
                     {'name':'results',        'len':None}],
                 'parsing':
                     [('results', lambda ble, original:
                        ble._parse_find_info_results(original['results'], original['format']))]},
            "0506":
                {'name':event.ATT_FindByTypeValueReq,
                 'structure':
                     [{'name':'conn_handle', 'len':2},
                     {'name':'pdu_len',        'len':1},
                     {'name':'start_handle','len':2},
                     {'name':'end_handle',    'len':2}]},
            "0507":
                {'name':event.ATT_FindByTypeValueRsp,
                 'structure':
                     [{'name':'conn_handle', 'len':2},
                     {'name':'pdu_len',        'len':1},
                     {'name':'start_handle','len':2},
                     {'name':'end_handle',    'len':2},
                     {'name':'value',        'len':None}]},
            "0508":
                {'name':event.ATT_ReadByTypeReq,
                 'structure':
                    [{'name':'conn_handle', 'len':2},
                     {'name':'pdu_len',        'len':1},
                     {'name':'start_handle','len':2},
                     {'name':'end_handle',    'len':2},
                     {'name':'type',        'len':None}]},
            "0509":
                {'name':event.ATT_ReadByTypeRsp,
                 'structure':
                     [{'name':'conn_handle',    'len':2},
                      {'name':'pdu_len',        'len':1},
                      {'name':'length',        'len':1},
                      {'name':'handle',        'len':2},
                      {'name':'value',        'len':None}]},
            "050b":
                {'name':event.ATT_ReadRsp,
                 'structure':
                     [{'name':'conn_handle',    'len':2},
                      {'name':'pdu_len',        'len':1},
                      {'name':'value',        'len':None}]},
            "050c":
                {'name':event.ATT_ReadBlobReq,
                 'structure':
                     [{'name':'conn_handle', 'len':2},
                     {'name':'pdu_len',        'len':1},
                     {'name':'handle',        'len':2},
                     {'name':'offset',        'len':2}]},
            "050d":
                {'name':event.ATT_ReadBlobRsp,
                 'structure':
                     [{'name':'conn_handle',    'len':2},
                      {'name':'pdu_len',        'len':1},
                      {'name':'value',        'len':None}]},
            "050f":
                {'name':event.ATT_ReadMultiRsp,
                 'structure':
                     [{'name':'conn_handle',    'len':2},
                      {'name':'pdu_len',        'len':1},
                      {'name':'results',        'len':None}]},
            "0510":
                {'name':event.ATT_ReadByGrpTypeReq,
                 'structure':
                     [{'name':'conn_handle', 'len':2},
                     {'name':'pdu_len',        'len':1},
                     {'name':'start_handle','len':2},
                     {'name':'end_handle',    'len':2},
                     {'name':'group_type',    'len':2}]},
            "0511":
                {'name':event.ATT_ReadByGrpTypeRsp,
                 'structure':
                     [{'name':'conn_handle', 'len':2},
                     {'name':'pdu_len',        'len':1}]},
            "0512":
                {'name':event.ATT_WriteReq,
                 'structure':
                     [{'name':'conn_handle', 'len':2},
                     {'name':'pdu_len',        'len':1},
                      {'name':'signature',     'len':1},
                     {'name':'command',        'len':1},
                     {'name':'handle',        'len':2},
                     {'name':'value',         'len':None}]},
            "0513":
                {'name':event.ATT_WriteRsp,
                 'structure':
                     [{'name':'conn_handle',    'len':2},
                      {'name':'pdu_len',        'len':1}]},
            "051b":
                {'name':event.ATT_HandleValueNotification,
                 'structure':
                     [{'name':'conn_handle',    'len':2},
                      {'name':'pdu_len',        'len':1},
                      {'name':'handle',        'len':2},
                      {'name':'values',        'len':None}]},
            "051d":
                {'name':event.ATT_HandleValueIndication,
                 'structure':
                     [{'name':'conn_handle',    'len':2},
                      {'name':'pdu_len',        'len':1},
                      {'name':'handle',        'len':2},
                      {'name':'values',        'len':None}]},
            "051e":
                {'name':event.ATT_HandleValueConfirmation,
                 'structure':
                    [{'name':'conn_handle',     'len':2}]},            
            "0580":
                {'name':event.GATT_ClientCharCfgUpdated,
                 'structure':
                    [{'name':'conn_handle', 'len':2},
                     {'name':'pdu_len',        'len':1},
                     {'name':'attr_handle', 'len':2},
                     {'name':'value',       'len':1}]},
            "0600":
                {'name':event.GAP_DeviceInitDone,
                 'structure':
                     [{'name':'dev_addr',    'len':6},
                      {'name':'data_pkt_len','len':2},
                      {'name':'num_data_pkts','len':1},
                      {'name':'irk',            'len':16},
                      {'name':'csrk',        'len':16}]},
            "0601":
                {'name':event.GAP_DeviceDiscoveryDone,
                 'structure':
                     [{'name':'num_devs',    'len':1},
                      {'name':'devices',        'len':None}],
                 'parsing': 
                     [('devices', lambda ble, original: 
                         ble._parse_devices(original['devices']))]},
            "0602":
                {'name':event.GAP_AdvertDataUpdateDone,
                 'structure':
                    [{'name':'ad_type',     'len':1}]},
            "0603":
                {'name':event.GAP_MakeDiscoverableDone,
                 'structure':
                     []},
            "0604":
                {'name':event.GAP_EndDiscoverableDone,
                 'structure':
                    []},
            "0605":
                {'name':event.GAP_LinkEstablished,
                 'structure':
                     [{'name':'dev_addr_type','len':1},
                      {'name':'dev_addr',    'len':6},
                      {'name':'conn_handle',    'len':2},
                      {'name':'conn_interval','len':2},
                      {'name':'conn_latency','len':2},
                      {'name':'conn_timeout','len':2},
                      {'name':'clock_accuracy','len':1}]},
            "0606":
                {'name':event.GAP_LinkTerminated,
                 'structure':
                     [{'name':'conn_handle', 'len':2},
                     {'name':'value',        'len':None}]},
            "0607":
                {'name':event.GAP_LinkParamUpdate,
                 'structure':
                     [{'name':'conn_handle', 'len':2},
                     {'name':'conn_interval', 'len':2},
                     {'name':'conn_latency',  'len':2},
                     {'name':'conn_timeout',  'len':2}]},
            "060d":
                {'name':event.GAP_DeviceInformation,
                 'structure':
                     [{'name':'event_type',    'len':1},
                      {'name':'addr_type',    'len':1},
                      {'name':'addr',        'len':6},
                      {'name':'rssi',        'len':1},
                      {'name':'data_len',    'len':1},
                      {'name':'data_field',    'len':None}]},
            "067f":
                {'name':event.GAP_HCI_ExtensionCommandStatus,
                 'structure':
                     [{'name':'op_code',        'len':2},
                      {'name':'data_len',    'len':1},
                      {'name':'param_value',    'len':None}],
                 'parsing':   
                     [('op_code', lambda ble, original: 
                         ble._parse_opcodes(original['op_code']))]},
            }