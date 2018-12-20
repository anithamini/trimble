import unittest
from source.PVT_functions import *
from util.common_func import *


class PVTsuite(unittest.TestCase):
    com = common()
    @classmethod
    def setUpClass(cls):
        def __init__(self):
            common.__init__(self)
            print("Object created")


    @classmethod
    def tearDownClass(cls):
       def __del__(self):
           common.__del__(self)
           print("Object destroyed")

    def test_start(self):
        self.assertEqual(self.com.start(), '$')

    def test_end(self):
        self.assertEqual(self.com.end(), '*')

    def test_Vendor_ID_presence(self):
        self.assertEqual(self.com.vendor_id_presence(), 1)

    def test_Vendor_ID_type(self):
        self.assertIs(self.com.vendor_id_type(), str)

    def test_Vendor_ID_size(self):
        self.assertEqual(self.com.vendor_id_size(), 8)

    def test_Firmware_version_presence(self):
        self.assertEqual(self.com.firmware_ver_presence(), 1)

    def test_Firmware_version_type(self):
        self.assertIs(self.com.firmware_ver_type(), str)

    def test_Firmware_version_size(self):
        self.assertEqual(self.com.firmware_ver_size(), 10)

    def test_Firmware_version_valid(self):
        self.assertEqual(self.com.firmware_ver_valid(), 1)

    def test_Packet_type_presence(self):
        self.assertEqual(packet_type_presence(), 1)

    def test_Packet_type_NR(self):
        self.assertEqual(packet_type_nr(), 'NR')

    def test_Packet_type_EA(self):
        self.assertEqual(packet_type_ea(), "EA")

    def test_Packet_type_TA(self):
        self.assertEqual(packet_type_ta(), "TA")

    def test_Packet_type_HP(self):
        self.assertEqual(packet_type_hp(), "HP")

    def test_Packet_type_IN(self):
        self.assertEqual(packet_type_in(), "IN")

    def test_Packet_type_IF(self):
        self.assertEqual(packet_type_if(), "IF")

    def test_Packet_type_BD(self):
        self.assertEqual(packet_type_bd(), "BD")

    def test_Packet_type_BR(self):
        self.assertEqual(packet_type_br(), "BR")

    def test_Packet_type_BL(self):
        self.assertEqual(packet_type_bl(), "BL")

    def test_Packet_type_valid(self):
        self.assertEqual(packet_type_valid(), 1)

    def test_Packet_status_presence(self):
        self.assertEqual(packet_status_presence(), 1)

    def test_Packet_status_Live(self):
        self.assertEqual(packet_status_live(), 'L')

    def test_Packet_status_history(self):
        self.assertEqual(packet_status_history(), 'H')

    def test_Packet_status_valid(self):
        self.assertEqual(packet_status_valid(), 1)

    def test_IMEI_presence(self):
        self.assertEqual(self.com.imei_presence(), 1)

    def test_IMEI_type(self):
        self.assertIs(self.com.imei_type(), str)

    def test_IMEI_size(self):
        self.assertEqual(self.com.imei_size(), 15)

    def test_IMEI_valid(self):
        self.assertEqual(self.com.imei_valid(), 1)

    def test_Vehicle_reg_presence(self):
        self.assertEqual(vehicle_reg_presence(), 1)

    def test_Vehicle_reg_size(self):
        self.assertEqual(vehicle_reg_size(), 10)

    def test_Vehicle_reg_type(self):
        self.assertIs(vehicle_reg_type(), str)

    def test_Vehicle_reg_valid(self):
        self.assertEqual(vehicle_reg_valid(), 1)

    def test_GPS_status_presence(self):
        self.assertEqual(gps_status_presence(), 1)

    def test_GPS_status_fix(self):
        self.assertEqual(gps_status_fix(), '1')

    def test_GPS_status_invalid(self):
        self.assertEqual(gps_status_invalid(), '0')

    def test_GPS_status_valid(self):
        self.assertEqual(gps_status_valid(), 1)

    def test_Date_presence(self):
        self.assertEqual(date_presence(), 1)

    def test_Date_type(self):
        self.assertIs(date_type(), str)

    def test_Date_valid(self):
        self.assertEqual(date_valid(), 1)

    def test_Time_presence(self):
        self.assertEqual(time_presence(), 1)

    def test_Time_type(self):
        self.assertIs(time_type(), str)

    def test_Time_valid(self):
        self.assertEqual(time_valid(), 1)

    def test_Latitude_presence(self):
        self.assertEqual(latitude_presence(), 1)

    def test_Latitude_size(self):
        self.assertEqual(latitude_size(), 12)

    def test_Latitude_type(self):
        self.assertIs(latitude_type(), float)

    def test_Latitude_valid(self):
        self.assertEqual(latitude_valid(), 1)

    def test_Latitude_dir_presence(self):
        self.assertEqual(latitude_dir_presence(), 1)

    def test_Latitude_dir_size(self):
        self.assertEqual(latitude_dir_size(), 1)

    def test_Latitude_dir_type(self):
        self.assertIs(latitude_dir_type(), str)

    def test_Latitude_dir_north(self):
        self.assertEqual(latitude_dir_north(), 'N')

    def test_Latitude_dir_south(self):
        self.assertEqual(latitude_dir_south(), 'S')

    def test_Latitude_dir_valid(self):
        self.assertEqual(latitude_dir_valid(), 1)

    def test_Longitude_presence(self):
        self.assertEqual(longitude_presence(), 1)

    def test_Longitude_size(self):
        self.assertEqual(longitude_size(), 12)

    def test_Longitude_type(self):
        self.assertIs(longitude_type(), float)

    def test_Longitude_valid(self):
        self.assertEqual(longitude_valid(), 1)

    def test_Longitude_dir_presence(self):
        self.assertEqual(long_dir_presence(), 1)

    def test_Longitude_dir_size(self):
        self.assertEqual(long_dir_size(), 1)

    def test_Longitude_dir_type(self):
        self.assertIs(long_dir_type(), str)

    def test_Longitude_dir_north(self):
        self.assertEqual(long_dir_east(), 'E')

    def test_Longitude_dir_south(self):
        self.assertEqual(long_dir_west(), 'W')

    def test_Longitude_dir_valid(self):
        self.assertEqual(long_dir_valid(), 1)

    def test_speed_presence(self):
        self.assertEqual(speed_presence(), 1)

    def test_speed_size(self):
        self.assertEqual(speed_size(), 6)

    def test_speed_type(self):
        self.assertIs(speed_type(), float)

    def test_speed_valid(self):
        self.assertEqual(speed_valid(), 1)

    def test_Heading_presence(self):
        self.assertEqual(heading_presence(), 1)

    def test_No_satellites_presence(self):
        self.assertEqual(no_satellites_presence(), 1)

    def test_No_satellites_type(self):
        self.assertIs(no_satellites_type(), int)

    def test_Altitude_presence(self):
        self.assertEqual(altitude_presence(), 1)

    def test_Altitude_size(self):
        self.assertEqual(altitude_size(), 12)

    def test_Altitude_valid(self):
        self.assertEqual(altitude_valid(), 1)

    def test_PDOP_presence(self):
        self.assertEqual(pdop_presence(), 1)

    def test_HDOP_presence(self):
        self.assertEqual(hdop_presence(), 1)

    def test_Net_operator_presence(self):
        self.assertEqual(net_operator_presence(), 1)

    def test_Net_operator_size(self):
        self.assertEqual(net_operator_size(), 7)

    def test_Net_operator_type(self):
        self.assertIs(net_operator_type(), str)

    def test_Main_power_status_presence(self):
        self.assertEqual(main_power_status_presence(), 1)

    def test_Main_power_status_on(self):
        self.assertEqual(main_power_status_on(), '1')

    def test_Main_power_status_off(self):
        self.assertEqual(main_power_status_off(), '0')

    def test_Main_power_status_valid(self):
        self.assertEqual(main_power_status_valid(), 1)

    def test_Main_input_voltage_presence(self):
        self.assertEqual(main_input_voltage_presence(), 1)

    def test_Main_input_voltage_valid(self):
        self.assertEqual(main_input_voltage_valid(), 1)

    def test_Internal_bat_volt_presence(self):
        self.assertEqual(internal_bat_volt_presence(), 1)

    def test_Internal_bat_volt_valid(self):
        self.assertEqual(internal_bat_volt_valid(), 1)

    def test_Ignition_presence(self):
        self.assertEqual(ignition_presence(), 1)

    def test_Ignition_on(self):
        self.assertEqual(ignition_on(), '1')

    def test_Ignition_off(self):
        self.assertEqual(ignition_off(), '0')

    def test_Emer_status_presence(self):
        self.assertEqual(emer_status_presence(), 1)

    def test_Emer_status_on(self):
        self.assertEqual(emer_status_on(), '1')

    def test_Emer_status_off(self):
        self.assertEqual(emer_status_off(), '0')

    def test_Tamper_alert_presence(self):
        self.assertEqual(tamper_alert_presence(), 1)

    def test_Tamper_alert_open(self):
        self.assertEqual(tamper_open(), 'O')

    def test_Tamper_alert_close(self):
        self.assertEqual(tamper_close(), 'C')

    def test_GSM_sig_strength_presence(self):
        self.assertEqual(gsm_sig_strength_presence(), 1)

    def test_GSM_sig_strength_valid(self):
        self.assertEqual(gsm_sig_strength_valid(), 1)

    def test_MCC_presence(self):
        self.assertEqual(mcc_presence(), 1)

    def test_MCC_size(self):
        self.assertEqual(mcc_size(), 3)

    def test_MCC_valid(self):
        self.assertEqual(mcc_valid(), 1)

    def test_MNC_presence(self):
        self.assertEqual(mnc_presence(), 1)

    def test_MNC_size(self):
        self.assertEqual(mnc_size(), 2)

    def test_MNC_valid(self):
        self.assertEqual(mnc_valid(), 1)

    def test_LAC_presence(self):
        self.assertEqual(lac_presence(), 1)

    def test_LAC_size(self):
        self.assertEqual(lac_size(), 4)

    def test_LAC_valid(self):
        self.assertEqual(lac_valid(), 1)

    def test_Cell_id_presence(self):
        self.assertEqual(cell_id_presence(), 1)

    def test_Cell_id_size(self):
        self.assertEqual(cell_id_size(), 4)

    def test_Cell_id_valid(self):
        self.assertEqual(cell_id_valid(), 1)

    def test_NMR_presence(self):
        self.assertEqual(nmr_presence(), 1)

    def test_Dig_input_presence(self):
        self.assertEqual(dig_input_presence(), 1)

    def test_Dig_input_size(self):
        self.assertEqual(dig_input_size(), 4)

    def test_Dig_input_valid(self):
        self.assertEqual(dig_input_valid(), 1)

    def test_Dig_output_presence(self):
        self.assertEqual(dig_output_presence(), 1)

    def test_Dig_output_size(self):
        self.assertEqual(dig_output_size(), 2)

    def test_Dig_output_valid(self):
        self.assertEqual(dig_output_valid(), 1)

    def test_Frame_num_presence(self):
        self.assertEqual(frame_num_presence(), 1)

    def test_Frame_num_size(self):
        self.assertEqual(frame_num_size(), 6)

    def test_Frame_num_valid(self):
        self.assertEqual(frame_num_valid(), 1)

    def test_Checksum_presence(self):
        self.assertEqual(checksum_presence(), 1)

    def test_Checksum_size(self):
        self.assertEqual(checksum_size(), 2)

    def test_Checksum_valid(self):
        self.assertEqual(checksum_valid(), 1)


if __name__ == '__main__':
    unittest.main()
    
    
    

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    

    




    

    

