import json
import re
pvt_json = '{ "START_CHARACTER":"$", ' \
    '"header":{"packet_info":"valid", "packet_type":"RT","vehicle_type":"EDC","packet_seq":"1","checksum":"10"},' \
    '"vendor_id":"12345678", "firmware_ver":"1234567890", "packet_type":"NR", "packet_status":"L",' \
    '"IMEI":"012345678901234","veh_reg_no":"DL1PC98212", "GPS_fix":"1", "date":"220714",' \
    '"time":"050656","latitude":28.758963,"lat_dir":"N","longitude":77.627784,"long_dir":"W","speed":25.1,' \
    '"Heading":"310.56","no_satellites":5,"Altitude":183.59788612,' \
    '"PDOP":"","HDOP":"","Net_operator":"INA Airtel","Main_power_status":"1","Main_input_voltage":"12.5",' \
    '"internal_bat_volt":"41.5","Ignition":"1","Emer_status":"1","tamper_alert":"C","gsm_sig_strength":25,' \
    '"MCC":"404","MNC":"10","LAC":"00D6","cell_id":"CFBD","NMR":"","Dig_input":"0001","Dig_output":"01",' \
    '"frame_num":"000005","checksum":"10","end_char":"*"}'
pvt = json.loads(pvt_json)


def packet_type_presence():  # to check packettype field presence
    global pvt
    if "packet_type" in pvt:
        return 1


def packet_type_nr():  # to check packet type field as NR or not
    global pvt
    if "packet_type" in pvt:
        return pvt["packet_type"]


def packet_type_ea():  # to check packettype field as EA or not
    global pvt
    if "packet_type" in pvt:
        return pvt["packet_type"]


def packet_type_ta():  # to check packettype field as TA or not
    global pvt
    if "packet_type" in pvt:
        return pvt["packet_type"]


def packet_type_hp():  # to check packettype field as HP or not
    global pvt
    if "packet_type" in pvt:
        return pvt["packet_type"]


def packet_type_in():  # to check packettype field as IN or not
    global pvt
    if "packet_type" in pvt:
        return pvt["packet_type"]


def packet_type_if():  # to check packettype field as IF or not
    global pvt
    if "packet_type" in pvt:
        return pvt["packet_type"]


def packet_type_bd():  # to check packettype field as BD or not
    global pvt
    if "packet_type" in pvt:
        return pvt["packet_type"]


def packet_type_br():  # to check packettype field as BR or not
    global pvt
    if "packet_type" in pvt:
        return pvt["packet_type"]


def packet_type_bl():  # to check packet type field as BL or not
    global pvt
    if "packet_type" in pvt:
        return pvt["packet_type"]


def packet_type_valid():  # to check the field value is valid or not
    global pvt
    total = ["BL", "BR", "BD", "IN", "IF", "HP", "TA", "EA", "NR"]
    if pvt["packet_type"] in total:
        return 1

    
def packet_status_presence():  # to check presence of packet status field
    global pvt
    if "packet_status" in pvt:
        return 1


def packet_status_live():  # to check packet status field as L
    global pvt
    if "packet_status" in pvt:
        return pvt["packet_status"]  # L


def packet_status_history():  # to check packet status field as H
    global pvt
    if "packet_status" in pvt:
        return pvt["packet_status"]  # H


def packet_status_valid():  # to check the field value is valid or not
    global pvt
    total = ["L", "H"]
    if pvt["packet_status"] in total:
        return 1


def vehicle_reg_presence():  # to check the presence of vehicle registration field
    global pvt
    if "veh_reg_no" in pvt:
        return 1


def vehicle_reg_size():  # to check the size of vehicle registration field
    global pvt
    if "veh_reg_no" in pvt:
        return len(pvt["veh_reg_no"])  # 10


def vehicle_reg_type():  # to check the type of vehicle registration field
    global pvt
    if "veh_reg_no" in pvt:
        return type(pvt["veh_reg_no"])  # str


def vehicle_reg_valid():  # to check the valid value of this field
    global pvt
    if "veh_reg_no" in pvt:
            if (len(pvt["veh_reg_no"]) == 10) and type(pvt["veh_reg_no"]) == str:
                if re.match("[0-9A-Z]*", pvt["veh_reg_no"]):
                    return 1

    
def gps_status_presence():  # to check the gps status field
    global pvt
    if "GPS_fix" in pvt:
        return 1


def gps_status_fix():  # to check gps field is fixed or not
    global pvt
    if "GPS_fix" in pvt:
        return pvt["GPS_fix"]  # 1


def gps_status_invalid():  # to check gps field is invalid or not
    global pvt
    if "GPS_fix" in pvt:
        return pvt["GPS_fix"]  # 0


def gps_status_valid():  # to check the valid value of this field
    global pvt
    if "GPS_fix" in pvt:
        if pvt["GPS_fix"] == '1' or pvt["GPS_fix"] == '0':
            return 1

    
def date_presence():  # to check the date presence field
    global pvt
    if "date" in pvt:
        return 1


def date_type():  # to check the date type
    global pvt
    if "date" in pvt:
        return type(pvt["date"])  # str


def date_valid():  # to check the valid value of this field
    global pvt
    if "date" in pvt and type(pvt["date"]) == str:
        if re.match("[0-9]", pvt["date"]):
            return 1
                              
        
def time_presence():  # to check the time presence field
    global pvt
    if "time" in pvt:
        return 1


def time_type():  # to check the date type
    global pvt
    if "time" in pvt:
        return type(pvt["time"])  # str


def time_valid():  # to check the valid value of this field
    global pvt
    if "time" in pvt and type(pvt["time"]) == str:
        if re.match("[0-9]", pvt["time"]):
            return 1


def latitude_presence():  # to check the latitude field presence
    global pvt
    if "latitude" in pvt:
        return 1


def latitude_size():  # to check the latitude size
    global pvt
    if "latitude" in pvt:
        return len(str(pvt["latitude"]))  # 12


def latitude_type():  # to check the latitude type
    global pvt
    if "latitude" in pvt:
        return type(pvt["latitude"])  # float


def latitude_valid():  # to check the value of the field is valid or not
    global pvt
    x = str(pvt["latitude"]).split('.')
    if len(x[0]) == 2 and len(x[1]) == 6:
        return 1

    
def latitude_dir_presence():  # to check the latitude direction field presence
    global pvt
    if "lat_dir" in pvt:
        return 1


def latitude_dir_size():  # to check the latitude direction field size
    global pvt
    if "lat_dir" in pvt:
        return len(pvt["lat_dir"])  # 1


def latitude_dir_type():  # to check the latitude direction field type
    global pvt
    if "lat_dir" in pvt:
        return type(pvt["lat_dir"])  # char


def latitude_dir_north():  # to check the latitude direction field as North or not
    global pvt
    if "lat_dir" in pvt:
        return pvt["lat_dir"]  # N


def latitude_dir_south():  # to check the latitude direction field as South or not
    global pvt
    if "lat_dir" in pvt:
        return pvt["lat_dir"]  # S


def latitude_dir_valid():  # to check the value of the field is valid or not
    global pvt
    if "lat_dir" in pvt:
        if pvt["lat_dir"] == 'N' or pvt["lat_dir"] == 'S':
            return 1

    
def longitude_presence():  # to check the longitude field presence
    global pvt
    if "longitude" in pvt:
        return 1


def longitude_size():  # to check the latitude field size
    global pvt
    if "longitude" in pvt:
        return len(str(pvt["longitude"]))  # 12


def longitude_type():  # to check the latitude field type
    global pvt
    if "longitude" in pvt:
        return type(pvt["longitude"])  # double


def longitude_valid():  # to check the value of the field is valid or not
    global pvt
    x = str(pvt["longitude"]).split('.')
    if len(x[0]) == 2 and len(x[1]) == 6:
        return 1


def long_dir_presence():  # to check the latitude direction field presence
    global pvt
    if "long_dir" in pvt:
        return 1


def long_dir_size():  # to check the latitude direction size
    global pvt
    if "long_dir" in pvt:
        return len(pvt["long_dir"])  # 1


def long_dir_type():  # to check the latitude direction type
    global pvt
    if "long_dir" in pvt:
        return type(pvt["long_dir"])  # 'char'


def long_dir_east():  # to check the latitude direction field as east or not
    global pvt
    if "long_dir" in pvt:
        return pvt["long_dir"]  # E


def long_dir_west():  # to check the latitude direction field as west or not
    global pvt
    if "long_dir" in pvt:
        return pvt["long_dir"]  # W


def long_dir_valid():  # to check the value of the field is valid or not
    global pvt
    if "long_dir" in pvt:
        if pvt["long_dir"] == 'E' or pvt["long_dir"] == 'W':
            return 1
    

def speed_presence():  # to check the speed field presence
    global pvt
    if "speed" in pvt:
        return 1


def speed_size():  # to check the speed field size
    global pvt
    if "speed" in pvt:
        return len(str(pvt["speed"]))  # 6


def speed_type():  # to check the speed field type
    global pvt
    if "speed" in pvt:
        return type(pvt["speed"])  # float


def speed_valid():  # to check the value of the field is valid or not
    global pvt
    if "speed" in pvt:
        if len(str(pvt["speed"])) == 6 and type(pvt["speed"]) == float:
            if re.match("[0-9.]*", str(pvt["speed"])) or pvt["speed"].isdigit():
                    return 1
             
         
def heading_presence():  # to check the heading field presence
    global pvt
    if "Heading" in pvt:
        return 1


def no_satellites_presence():  # to check the No of satellites field presence
    global pvt
    if "no_satellites" in pvt:
        return 1


def no_satellites_type():  # to check the No of satellites field type
    global pvt
    if "no_satellites" in pvt:
        return type(pvt["no_satellites"])  # int


def altitude_presence():  # to check the Altitude field presence
    global pvt
    if "Altitude" in pvt:
        return 1


def altitude_size():  # to check the Altitude field size
    global pvt
    if "Altitude" in pvt:
        return len(str(pvt["Altitude"]))  # 12


def altitude_valid():  # to check the value of the field is valid or not
    global pvt
    if "Altitude" in pvt:
        if len(str(pvt["Altitude"])) == 12 and type(pvt["Altitude"]) == float:
            if re.match("[0-9.]*", str(pvt["Altitude"])) or pvt["Altitude"].isdigit():
                    return 1

   
def pdop_presence():  # to check the PDOP field presence
    global pvt
    if "PDOP" in pvt:
        return 1


def hdop_presence():  # to check the HDOP field presence
    global pvt
    if "HDOP" in pvt:
        return 1


def net_operator_presence():  # to check the N/W operator field presence
    global pvt
    if "Net_operator" in pvt:
        return 1


def net_operator_size():  # to check the N/W operator field size
    global pvt
    if "Net_operator" in pvt:
        return len(pvt["Net_operator"])  # 7


def net_operator_type():  # to check the N/W operator field type
    global pvt
    if "Net_operator" in pvt:
        return type(pvt["Net_operator"])  # char


def main_power_status_presence():  # to check the main_power_status field presence
    global pvt
    if "Main_power_status" in pvt:
        return 1


def main_power_status_on():  # to check the vehicle battery reconnection
    global pvt
    if "Main_power_status" in pvt:
        return pvt["Main_power_status"]  # 1


def main_power_status_off():  # to check the vehicle battery disconnection
    global pvt
    if "Main_power_status" in pvt:
        return pvt["Main_power_status"]  # 0


def main_power_status_valid():  # to check the value of the field is valid or not
    global pvt
    if "Main_power_status" in pvt:
        if pvt["Main_power_status"] == '1' or pvt["Main_power_status"] == '0':
            return 1

    
def main_input_voltage_presence():  # to check the main_input_voltage field presence
    global pvt
    if "Main_input_voltage" in pvt:
        return 1


def main_input_voltage_valid():  # to check the value of the field is valid or not
    global pvt
    if "Main_input_voltage" in pvt:
            if re.match("[0-9.]*", pvt["Main_input_voltage"]) or pvt["Main_input_voltage"].isdigit():
                    return 1


def internal_bat_volt_presence():  # to check the internal_bat_voltage field presence
    global pvt
    if "internal_bat_volt" in pvt:
        return 1


def internal_bat_volt_valid():  # to check the value of the field is valid or not
    global pvt
    if "internal_bat_volt" in pvt:
            if re.match("[0-9.]*", pvt["internal_bat_volt"]) or pvt["internal_bat_volt"].isdigit():
                    return 1


def ignition_presence():  # to check the ignition field presence
    global pvt
    if "Ignition" in pvt:
        return 1


def ignition_on():  # to check the ignition on or not
    global pvt
    if "Ignition" in pvt:
        return pvt["Ignition"]  # 1


def ignition_off():  # to check the ignition off or not
    global pvt
    if "Ignition" in pvt:
        return pvt["Ignition"]  # 0


def ignition_valid():  # to check the value of the field is valid or not
    global pvt
    if "ignition" in pvt:
        if pvt["ignition"] == '1' or pvt["ignition"] == '0':
            return 1


def emer_status_presence():  # to check the emergency status field presence
    global pvt
    if "Emer_status" in pvt:
        return 1


def emer_status_on():  # to check the emergency status on or not
    global pvt
    if "Emer_status" in pvt:
        return pvt["Emer_status"]  # 1


def emer_status_off():  # to check the emergency status off or not
    global pvt
    if "Emer_status" in pvt:
        return pvt["Emer_status"]  # 0


def emer_status_valid():  # to check the value of the field is valid or not
    global pvt
    if "Emer_status" in pvt:
        if pvt["Emer_status"] == '1' or pvt["Emer_status"] == '0':
            return 1


def tamper_alert_presence():  # to check the tamper alert field presence
    global pvt
    if "tamper_alert" in pvt:
        return 1


def tamper_open():  # to check the tamper alert status
    global pvt
    if "tamper_alert" in pvt:
        return pvt["tamper_alert"]  # O


def tamper_close():  # to check the tamper alert status
    global pvt
    if "tamper_alert" in pvt:
        return pvt["tamper_alert"]  # C


def tamper_field_valid():  # to check the value of the field is valid or not
    global pvt
    if "tamper_alert" in pvt:
        if pvt["tamper_alert"] == 'C' or pvt["tamper_alert"] == 'O':
            return 1


def gsm_sig_strength_presence():  # to check the gsm signal strength field presence
    global pvt
    if "gsm_sig_strength" in pvt:
        return 1


def gsm_sig_strength_valid():  # to check the value of the field is valid or not
    global pvt
    if 0 <= pvt["gsm_sig_strength"] <= 31:
        return 1


def mcc_presence():  # to check the mcc field presence
    global pvt
    if "MCC" in pvt:
        return 1


def mcc_size():  # to check the mcc field size
    global pvt
    if "MCC" in pvt:
        return len(pvt["MCC"])  # 3


def mcc_valid():  # to check the value of the field is valid or not
    global pvt
    if "MCC" in pvt:
            if re.match("[0-9]", pvt["MCC"]):
                    return 1


def mnc_presence():  # to check the mnc field presence
    global pvt
    if "MNC" in pvt:
        return 1


def mnc_size():  # to check the mnc field size
    global pvt
    if "MNC" in pvt:
        return len(pvt["MNC"])  # 2


def mnc_valid():  # to check the value of the field is valid or not
    global pvt
    if "MNC" in pvt:
            if re.match("[0-9]", pvt["MNC"]):
                    return 1


def lac_presence():  # to check the lac field presence
    global pvt
    if "LAC" in pvt:
        return 1


def lac_size():  # to check the lac field size
    global pvt
    if "LAC" in pvt:
        return len(pvt["LAC"])  # 4


def lac_valid():  # to check the value of the field is valid or not
    global pvt
    if "LAC" in pvt:
            if re.match("[A-Z0-9]", pvt["LAC"]):
                    return 1


def cell_id_presence():  # to check the cell id field presence
    global pvt
    if "cell_id" in pvt:
        return 1


def cell_id_size():  # to check the cell id field size
    global pvt
    if "cell_id" in pvt:
        return len(pvt["cell_id"])  # 4


def cell_id_valid():  # to check the value of the field is valid or not
    global pvt
    if "cell_id" in pvt:
            if re.match("[A-Z]", pvt["cell_id"]):
                    return 1


def nmr_presence():  # to check the nmr field presence
    global pvt
    if "NMR" in pvt:
        return 1


def dig_input_presence():  # to check the digital input field presence
    global pvt
    if "Dig_input" in pvt:
        return 1


def dig_input_size():  # to check the digital input field size
    global pvt
    if "Dig_input" in pvt:
        return len(pvt["Dig_input"])  # 4


def dig_input_valid():  # to check the value of the field is valid or not
    global pvt
    if "Dig_input" in pvt:
            if re.match("[0-1]", pvt["Dig_input"]):
                    return 1


def dig_output_presence():  # to check the digital output field presence
    global pvt
    if "Dig_output" in pvt:
        return 1


def dig_output_size():  # to check the digital output field size
    global pvt
    if "Dig_output" in pvt:
        return len(pvt["Dig_output"])  # 2


def dig_output_valid():  # to check the value of the field is valid or not
    global pvt
    if "Dig_output" in pvt:
            if re.match("[0-1]", pvt["Dig_output"]):
                    return 1


def frame_num_presence():  # to check the frame number field presence
    global pvt
    if "frame_num" in pvt:
        return 1


def frame_num_size():  # to check the frame number field size
    global pvt
    if "frame_num" in pvt:
        return len(pvt["frame_num"])  # 6


def frame_num_valid():  # to check the value of the field is valid or not
    global pvt
    if 1 <= int(pvt["frame_num"]) <= 999999:
        return 1


def checksum_presence():  # to check the checksum field presence
    global pvt
    if "checksum" in pvt:
        return 1


def checksum_size():  # to check the checksum field size
    global pvt
    if "checksum" in pvt:
        return len(pvt["checksum"])  # 2


def checksum_valid():  # to check the value of the field is valid or not
    global pvt
    if "checksum" in pvt:
            if re.match("[0-9]", pvt["checksum"]):
                    return 1
