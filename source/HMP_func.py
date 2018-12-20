import json
hmp_json = '{ "start_character":"$", ' \
   '"header":{"packet_info":"valid","packet_type":"RT","vehicle_type":"EDC","packet_seq":"1","checksum":"10"},' \
   '"vendor_id":"12345678","firmware_ver":"12.66.34.7","IMEI":"012345678901234","battery_per":"56",' \
   '"lowBattery":"14","memory_per":"69","IGN_on":"130","IGN_off":"0","Dig_i/o":"0001","ang_i/o":"010","end_char":"*"}'

hmp = json.loads(hmp_json)
"""
No idea on vendor_id,header,ign_on,ign_off,dig_io,ang_io
"""


def battery_per_presence():  # To check the battery percentage presence
    global hmp
    if "battery_per" in hmp:
        return 1


def valid_battery_per():    # to check the valid battery percentage
    global hmp
    if "battery_per" in hmp:
        if hmp["battery_per"].isdigit():
            return 1


def low_battery_per_presence():  # to check the presence of low battery percentage
    global hmp
    if "lowBattery" in hmp:
        return 1


def valid_low_battery_per():    # to check the valid low battery percentage
    global hmp
    if "lowBattery" in hmp:
        if hmp["lowBattery"].isdigit():
            return 1


def memory_per_presence():  # to check the presence of memory percentage
    global hmp
    if "memory_per" in hmp:
        return 1


def valid_memory_per():  # to check the valid memory percentage
    global hmp
    if "memory_per" in hmp:
        if hmp["memory_per"].isdigit():
            return 1


def ign_on_presence():  # to check the presence of ignition on
    global hmp
    if "IGN_on" in hmp:
        return 1


def ign_off_presence():    # to check the presence of ignition off
    global hmp
    if "IGN_off" in hmp:
        return 1


def digital_io():   # to check the presence of digital i/o status
    global hmp
    if "Dig_i/o" in hmp:
        return 1


def analog_io():    # to check the presence of analog i/o status
    global hmp
    if "ang_i/o" in hmp:
        return 1
