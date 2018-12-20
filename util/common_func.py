import json
import re
com_para_json = '{ "start_character":"$","vendor_id":"12345678","firmware_ver":"12.66.34.7",' \
           '"IMEI":"012345678901234","end_char":"*"}'

com_para = json.loads(com_para_json)


class common:

    @classmethod
    def setUpClass(cls):
        def __init__(self):
            print("Object created")

    @classmethod
    def tearDownClass(cls):
        def __del__(self):
            print("Object destroyed")

    @staticmethod
    def start():    # to check the start character in a frame
        global com_para
        if "start_character" in com_para:
            return com_para["start_character"]

    @staticmethod
    def end():  # to check the start character in a frame
        global com_para
        if "end_char" in com_para:
            return com_para["end_char"]

    @staticmethod
    def vendor_id_presence():   # to check the presence of vendor_ID
        global com_para
        if "vendor_id" in com_para:
            return 1

    @staticmethod
    def vendor_id_size():       # to check the size of the vendor_ID
        global com_para
        if "vendor_id" in com_para:
            return len(com_para["vendor_id"])

    @staticmethod
    def vendor_id_type():   # to check the type of the vendor_ID
        global com_para
        if "vendor_id" in com_para:
            return type(com_para["vendor_id"])

    @staticmethod
    def firmware_ver_presence():    # to check the presence of firmware version
        global com_para
        if "firmware_ver" in com_para:
            return 1

    @staticmethod
    def firmware_ver_size():       # to check the size of firmware version
        global com_para
        if "firmware_ver" in com_para:
            return len(com_para["firmware_ver"])

    @staticmethod
    def firmware_ver_valid():      # to check the valid firmware version
        global com_para
        if "firmware_ver" in com_para:
            if (len(com_para["firmware_ver"]) == 10) and type(com_para["firmware_ver"]) == str:
                if re.match("[0-9.]*", com_para["firmware_ver"]):
                    return 1

    @staticmethod
    def firmware_ver_type():    # to check the type of the firmware version
        global com_para
        if "firmware_ver" in com_para:
            return type(com_para["firmware_ver"])

    @staticmethod
    def imei_presence():    # to check the presence of IMEI number
        global com_para
        if "IMEI" in com_para:
            return 1

    @staticmethod
    def imei_size():    # to check the size of IMEI number
        global com_para
        if "IMEI" in com_para:
            return len(com_para["IMEI"])

    @staticmethod
    def imei_type():    # to check the type of IMEI number
        global com_para
        if "IMEI" in com_para:
            return type(com_para["IMEI"])

    @staticmethod
    def imei_valid():   # to check the valid IMEI number
        global com_para
        if "IMEI" in com_para:
            if (len(com_para["IMEI"]) == 15) and type(com_para["IMEI"]) == str:
                if re.match("[0-9]", com_para["IMEI"]):
                    return 1
                else:
                    return 0