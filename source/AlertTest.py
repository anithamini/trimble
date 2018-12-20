import unittest
from source.Alert import *


class Alertsuite(unittest.TestCase):
    def test_msg_presence(self):                                 # to check the msg presence in the alert
        self.assertEqual(msg_presence(), 1)

    def test_msg_type(self):                                     # to check the message type in the alert
        self.assertEqual(msg_type(), 1)

    def test_msg_data_type(self):                                # to check the data type of msg in the alert
        self.assertIs(msg_data_type(), str)

    def test_msg_size(self):                                     # to check the length of the msg in the alert
        self.assertEqual(msg_size(), 2)
# ------------------------------------------------------#

    def test_imei_presence(self):                                # to check the IMEI presence in the alert message
        self.assertEqual(imei_presence(), 1)

    def test_imei_size(self):                                   # to check the length of IMEI in the alert message
        self.assertEqual(imei_size(), 15)

    def test_imei_type(self):                                   # to check the data type of IMEI in the alert messgae
        self.assertIs(imei_data_type(), str)

    def test_valid_imei(self):
        self.assertEqual(imei_valid(), 1)                      # to check the valid IMEI number
# ------------------------------------------------------#

    def test_pckt_presence(self):                             # to check the Packet presence in the alert message
        self.assertEqual(pckt_presence(), 1)

    def test_pckt_size(self):                                  # to check the length of the packet in the alert message
        self.assertEqual(pckt_size(), 2)

    def test_pckt_data_type(self):                        # to check the datatype of the packet in the alert message
        self.assertIs(pckt_data_type(), str)

    def test_pckt_type(self):                                   # to check the packet type in the alert message
        self.assertEqual(pckt_type(), 1)
# --------------------------------------------------------#

    def test_date_time_presence(self):                  # to check the presence of date and time in the alert message
        self.assertEqual(date_time_presence(), 1)

    def test_date_time_size(self):                              # to check the length of the date and time
        self.assertEqual(date_time_size(), 14)

    def test_date_time_data_type(self):                         # to check the data type of the date and time
        self.assertIs(date_time_data_type(), str)

    def test_valid_date_time(self):
        self.assertEqual(valid_date_time(), 1)                  # to check the valid date and time
# ---------------------------------------------------------#

    def test_gps_validity_presence(self):                       # to check the presence of GPS validity
        self.assertEqual(gps_validity_presence(), 1)

    def test_gps_validity_size(self):                  # to check the length of the GPS validity in the alert message
        self.assertEqual(gps_validity_size(), 1)

    def test_gps_validity_data_type(self):                      # to check teh data type of the GPS validity
        self.assertIs(gps_validity_data_type(), str)

    def test_gps_validity_type(self):                          # to check the type of GPS validity in the alert message
        self.assertEqual(gps_validity_type(), 1)
# ----------------------------------------------------------#

    def test_latitude_presence(self):               # to check the presence of the latitude value in the alert message
        self.assertEqual(latitude_presence(), 1)

    def test_latitude_size(self):                              # to check the length of the latitude value
        self.assertEqual(latitude_size(), 12)

    def test_latitude_data_type(self):                         # to check the data type of the latitude value
        self.assertIs(latitude_data_type(), float)

    def test_valid_latitude(self):
        self.assertEqual(valid_latitude(), 1)                   # to check the valid latitude
# ----------------------------------------------------------#

    def test_lat_dir_presence(self):        # to check the presence of latitude direction value in the alert message
        self.assertEqual(lat_dir_presence(), 1)

    def test_lat_dir_size(self):                      # to check the length of the latitude direction value
        self.assertEqual(lat_dir_size(), 1)

    def test_lat_dir_data_type(self):              # to check the data type of the latitude direction in alert message
        self.assertIs(lat_dir_data_type(), str)

    def test_lat_dir_type(self):                 # to check the type of the latitude direction value in alert message
        self.assertEqual(lat_dir_type(), 1)
# ----------------------------------------------------------#

    def test_longitude_presence(self):            # to check the presence of the longitude value in the alert message
        self.assertEqual(longitude_presence(), 1)

    def test_longitude_size(self):                           # to check the length of the longitude value
        self.assertEqual(longitude_size(), 12)

    def test_longitude_data_type(self):                      # to check the data type of the longitude value
        self.assertIs(longitude_data_type(), float)

    def test_valid_longitude(self):
        self.assertEqual(valid_longitude(), 1)                   # to check the valid longitude
# -----------------------------------------------------------#

    def test_long_dir_presence(self):     # to check the presence of longitude direction value in the alert message
        self.assertEqual(long_dir_presence(), 1)

    def test_long_dir_size(self):                            # to check the length of the longitude direction value
        self.assertEqual(long_dir_size(), 1)

    def test_long_dir_data_type(self):         # to check the data type of the longitude direction in alert message
        self.assertIs(long_dir_data_type(), str)

    def test_long_dir_type(self):   # to check the type of the longitude direction value in alert message
        self.assertEqual(long_dir_type(), 1)
# ----------------------------------------------------------#

    def test_altitude_presence(self):      # to check the presence of the altitude value in the alert message
        self.assertEqual(altitude_presence(), 1)

    def test_altitude_size(self):                            # to check the length of the altitude value
        self.assertEqual(altitude_size(), 12)

    def test_altitude_data_type(self):                       # to check the data type of the altitude value
        self.assertIs(altitude_data_type(), float)

    def test_valid_altitude(self):
        self.assertEqual(valid_altitude(), 1)                   # to check the valid altitude
# ------------------------------------------------------------#

    def test_speed_presence(self):                  # to check the presence of the speed value in the alert message
        self.assertEqual(speed_presence(), 1)

    def test_speed_size(self):                               # to check the length of the speed value
        self.assertEqual(speed_size(), 6)

    def test_speed_data_type(self):                          # to check the data type of the speed value
        self.assertIs(speed_data_type(), float)

    def test_valid_speed(self):
        self.assertEqual(valid_speed(), 1)                   # to check the valid speed
# ------------------------------------------------------------#

    def test_direction_presence(self):           # to check the presence of the Direction value in the alert message
        self.assertEqual(direction_presence(), 1)

    def test_direction_size(self):                           # to check the length of the Direction value
        self.assertEqual(direction_size(), 6)

    def test_direction_data_type(self):                      # to check the data type of the Direction value
        self.assertIs(direction_data_type(), float)

    def test_valid_direction(self):
        self.assertEqual(valid_direction(), 1)                   # to check the valid direction
# ------------------------------------------------------------#

    def test_gps_provider_presence(self):      # to check the presence of the GPS provider value in the alert message
        self.assertEqual(gps_provider_presence(), 1)

    def test_gps_provider_size(self):                        # to check the length of the GPS provider value
        self.assertEqual(gps_provider_size(), 1)

    def test_gps_provider_data_type(self):                   # to check the data type of the GPS provider value
        self.assertIs(gps_provider_data_type(), str)

    def test_gps_provider_type(self):            # to check the type of the GPS provider value in alert message
        self.assertEqual(gps_provider_type(), 1)
# -----------------------------------------------------------#

    def test_vehicle_reg_num_presence(self):
        # to check the presence of the Vehicle registration number value in the alert message
        self.assertEqual(vehicle_reg_num_presence(), 1)

    def test_vehicle_reg_num_size(self):             # to check the length of the Vehicle registration number value
        self.assertEqual(vehicle_reg_num_size(), 16)

    def test_vehicle_reg_num_data_type(self):        # to check the data type of the Vehicle registration number value
        self.assertIs(vehicle_reg_num_data_type(), str)

    def test_valid_vehicle_num(self):
        self.assertEqual(valid_vehicle_num(), 1)
# -----------------------------------------------------------#

    def test_reply_num_presence(self):          # to check the presence of the Reply number value in the alert message
        self.assertEqual(reply_num_presence(), 1)

    def test_reply_num_size(self):                  # to check the length of the Reply number value
        self.assertEqual(reply_num_size(), 10)

    def test_valid_reply_num(self):
        self.assertEqual(valid_reply_num(), 1)      # to check the valid reply number
# -------------------------------------------------------------#

    def test_checksum_presence(self):  # to check the presence of the Checksum value in the alert message
        self.assertEqual(checksum_presence(), 1)

    def test_checksum_size(self):                            # to check the length of the Checksum number value
        self.assertEqual(checksum_size(), 8)

    def test_valid_checksum(self):
        self.assertEqual(valid_checksum_num(), 1)           # to check the valid checksum


if __name__ == '__main__':
    unittest.main()
