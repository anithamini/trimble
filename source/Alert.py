import json
import re
import numpy as np
alert_data = '{"header":{"packet_info":"valid","packet_type":"RT","vehicle_type":"EDC","packet_seq":"1",' \
            '"checksum":"10"}, "message_type":"EMR","IMEI":"012345678901234","packet_type":"NM",' \
            '"date_time":"22072014050656","gps_val":"A","latitude":28.758963,"lat_dir":"N",' \
            '"longitude":77.6277844,"long_dir":"W","Altitude":183.54564564,"speed":25.632,"direction":25.632,' \
             '"veh_reg_no":"DL1PC98212","gps_provider":"G","reply_num":"9849058167","checksum":"10000000"}'

alert_json = json.loads(alert_data)

# ****************** Message type Test cases ************************* #


def msg_presence():
    global alert_json
    if "message_type" in alert_json:
        return 1


def msg_data_type():
    global alert_json
    if "message_type" in alert_json:
        return type(alert_json["message_type"])


def msg_type():
    global alert_json
    if "message_type" in alert_json and (alert_json["message_type"] == "EMR" or alert_json["message_type"] == "SEM"):
        return 1


def msg_size():
    global alert_json
    if "message_type" in alert_json:
        return len(alert_json["message_type"])

# ****************** IMEI Test cases ************************* #


def imei_presence():
    global alert_json
    if "IMEI" in alert_json:
        return 1


def imei_size():
    global alert_json
    if "IMEI" in alert_json:
        return len(alert_json["IMEI"])


def imei_data_type():
    global alert_json
    if "IMEI" in alert_json:
        return type(alert_json["IMEI"])


def imei_valid():   # to check the valid IMEI number
        global alert_json
        if "IMEI" in alert_json:
            if (len(alert_json["IMEI"]) == 15) and type(alert_json["IMEI"]) == str:
                if re.match("[0-9]", alert_json["IMEI"]):
                    return 1
                else:
                    return 0

# ****************** Packet type Test cases ************************* #


def pckt_presence():
    global alert_json
    if "packet_type" in alert_json:
        return 1


def pckt_size():
    global alert_json
    if "packet_type" in alert_json:
        return len(alert_json["packet_type"])


def pckt_data_type():
    global alert_json
    if "packet_type" in alert_json:
        return type(alert_json["packet_type"])


def pckt_type():
    global alert_json
    if "packet_type" in alert_json and (alert_json["packet_type"] == "NM" or alert_json["packet_type"] == "SP"):
        return 1

# ****************** Date & Time Test cases ************************* #


def date_time_presence():
    global alert_json
    if "date_time" in alert_json:
        return 1


def date_time_size():
    global alert_json
    if "date_time" in alert_json:
        return len(alert_json["date_time"])


def date_time_data_type():
    global alert_json
    if "date_time" in alert_json:
        return type(alert_json["date_time"])


def valid_date_time():
    global alert_json
    if "date_time" in alert_json and alert_json["date_time"].isdigit():
        return 1

# ****************** GPS validity Test cases ************************* #


def gps_validity_presence():
    global alert_json
    if "gps_val" in alert_json:
        return 1


def gps_validity_size():
    global alert_json
    if "gps_val" in alert_json:
        return len(alert_json["gps_val"])


def gps_validity_type():
    global alert_json
    if "gps_val" in alert_json and alert_json["gps_val"] == 'A' or alert_json["gps_val"] == 'V':
        return 1


def gps_validity_data_type():
    global alert_json
    if "gps_val" in alert_json:
        return type(alert_json["gps_val"])

# ****************** Latitude Test cases ************************* #


def latitude_presence():
    global alert_json
    if "latitude" in alert_json:
        return 1


def latitude_size():
    global alert_json
    if "latitude" in alert_json:
        return len(str(alert_json["latitude"]))


def latitude_data_type():
    global alert_json
    if "latitude" in alert_json:
        return type(alert_json["latitude"])


def valid_latitude():
    global alert_json
    if "latitude" in alert_json:
        x = str(alert_json["latitude"]).split('.')
        if len(x[0]) == 2 and len(x[1]) == 6:
            return 1

        # ****************** Latitude_Direction Test cases ************************* #


def lat_dir_presence():
    global alert_json
    if "lat_dir" in alert_json:
        return 1


def lat_dir_size():
    global alert_json
    if "lat_dir" in alert_json:
        return len(alert_json["lat_dir"])


def lat_dir_data_type():
    global alert_json
    if "lat_dir" in alert_json:
        return type(alert_json["lat_dir"])


def lat_dir_type():
    global alert_json
    if "lat_dir" in alert_json and (alert_json["lat_dir"] == "N" or alert_json["lat_dir"] == "S"):
        return 1

# ****************** Longitude Test cases ************************* #


def longitude_presence():
    global alert_json
    if "longitude" in alert_json:
        return 1


def longitude_size():
    global alert_json
    if "longitude" in alert_json:
        return len(str(alert_json["longitude"]))


def longitude_data_type():
    global alert_json
    if "longitude" in alert_json:
        return type(alert_json["longitude"])


def valid_longitude():
    global alert_json
    if "longitude" in alert_json:
        x = str(alert_json["longitude"]).split('.')
        if len(x[0]) == 2 and len(x[1]) == 6:
            return 1

# ****************** Latitude_Direction Test cases ************************* #


def long_dir_presence():
    global alert_json
    if "long_dir" in alert_json:
        return 1


def long_dir_size():
    global alert_json
    if "long_dir" in alert_json:
        return len(alert_json["long_dir"])


def long_dir_data_type():
    global alert_json
    if "long_dir" in alert_json:
        return type(alert_json["long_dir"])


def long_dir_type():
    global alert_json
    if "long_dir" in alert_json and (alert_json["long_dir"] == "W" or alert_json["long_dir"] == "E"):
        return 1

# ****************** Altitude Test cases ************************* #


def altitude_presence():
    global alert_json
    if "Altitude" in alert_json:
        return 1


def altitude_size():
    global alert_json
    if "Altitude" in alert_json:
        return len(str(alert_json["Altitude"]))


def altitude_data_type():
    global alert_json
    if "Altitude" in alert_json:
        return type(alert_json["Altitude"])


def valid_altitude():
    global alert_json
    if "Altitude" in alert_json:
        if (len(str(alert_json["Altitude"]))) == 12 and type(alert_json["Altitude"]) == float:
            if (re.match("[0-9.]*", str(alert_json["Altitude"]))) or alert_json["Altitude"].isdigit():
                return 1

# ****************** Speed Test cases ************************* #


def speed_presence():
    global alert_json
    if "speed" in alert_json:
        return 1


def speed_size():
    global alert_json
    if "speed" in alert_json:
        return len(str(alert_json["speed"]))


def speed_data_type():
    global alert_json
    if "speed" in alert_json:
        return type(alert_json["speed"])


def valid_speed():
    global alert_json
    if "speed" in alert_json:
        if len(str(alert_json["speed"])) == 6 and type(alert_json["speed"]) == float:
            if (re.match("[0-9.]*", str(alert_json["speed"]))) or alert_json["speed"].isdigit():
                return 1

    # ****************** Direction Test cases ************************* #


def direction_presence():
    global alert_json
    if "direction" in alert_json:
        return 1


def direction_size():
    global alert_json
    if "direction" in alert_json:
        return len(str(alert_json["direction"]))


def direction_data_type():
    global alert_json
    if "direction" in alert_json:
        return type(alert_json["direction"])


def valid_direction():
    global alert_json
    if "direction" in alert_json:
        if (len(str(alert_json["direction"]))) == 6 and type(alert_json["direction"]) == float:
            if (re.match("[0-9.]*", str(alert_json["direction"]))) or alert_json["direction"].isdigit():
                return 1

# ****************** GPS Provider Test cases ************************* #


def gps_provider_presence():
    global alert_json
    if "gps_provider" in alert_json:
        return 1


def gps_provider_size():
    global alert_json
    if "gps_provider" in alert_json:
        return len(alert_json["gps_provider"])


def gps_provider_type():
    global alert_json
    if "gps_provider" in alert_json and (alert_json["gps_provider"] == "G" or alert_json["gps_provider"] == "N"):
        return 1


def gps_provider_data_type():
    global alert_json
    if "gps_provider" in alert_json:
        return type(alert_json["gps_provider"])

# ****************** Vehicle Registration Number Test cases ************************* #


def vehicle_reg_num_presence():
    global alert_json
    if "veh_reg_no" in alert_json:
        return 1


def vehicle_reg_num_size():
    global alert_json
    if "veh_reg_no" in alert_json:
        return len(alert_json["veh_reg_no"])


def vehicle_reg_num_data_type():
    global alert_json
    if "veh_reg_no" in alert_json:
        return type(alert_json["veh_reg_no"])


def valid_vehicle_num():
    global alert_json
    if "veh_reg_no" in alert_json and re.match("[0-9A-Z]",alert_json["veh_reg_no"]) and type(alert_json["veh_reg_no"]) == str \
            and len(alert_json["veh_reg_no"]) == 16:
        return 1

# ****************** Reply Number Test cases ************************* #


def reply_num_presence():
    global alert_json
    if "reply_num" in alert_json:
        return 1


def reply_num_size():
    global alert_json
    if "reply_num" in alert_json:
        return len(alert_json["reply_num"])


def valid_reply_num():
    global alert_json
    if "reply_num" in alert_json and len(alert_json["reply_num"]) == 10 and alert_json["reply_num"].isdigit():
        return 1


# ****************** Check-sum Test cases ************************* #


def checksum_presence():
    global alert_json
    if "checksum" in alert_json:
        return 1


def checksum_size():
    global alert_json
    if "checksum" in alert_json:
        return len(alert_json["checksum"])


def valid_checksum_num():
    global alert_json
    if "checksum" in alert_json and len(alert_json["checksum"]) == 8 and alert_json["checksum"].isdigit():
        return 1