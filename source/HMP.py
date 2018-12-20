import unittest
from source.HMP_func import *
from util.common_func import *


class HMPsuite(unittest.TestCase):
    com = common()

    @classmethod
    def setUpClass(cls):
        def __init__(self):
            common. __init__(self)
            print("Object created")

    @classmethod
    def tearDownClass(cls):
        def __del__(self):
            common. __del__(self)
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

    def test_IMEI_presence(self):
        self.assertEqual(self.com.imei_presence(), 1)

    def test_IMEI_type(self):
        self.assertIs(self.com.imei_type(), str)

    def test_IMEI_size(self):
        self.assertIs(self.com.imei_size(), 15)

    def test_IMEI_valid(self):
        self.assertEqual(self.com.imei_valid(), 1)

    def test_Battery_per_presence(self):
        self.assertEqual(battery_per_presence(), 1)

    def test_valid_battery_per(self):
        self.assertEqual(valid_battery_per(), 1)

    def test_Low_Battery_per_presence(self):
        self.assertEqual(low_battery_per_presence(), 1)

    def test_valid_low_battery_per(self):
        self.assertEqual(valid_low_battery_per(), 1)

    def test_Memory_per_presence(self):
        self.assertEqual(memory_per_presence(), 1)

    def test_valid_memory_per(self):
        self.assertEqual(valid_memory_per(), 1)

    def test_IGN_ON_presence(self):
        self.assertEqual(ign_on_presence(), 1)

    def test_IGN_OFF_presence(self):
        self.assertEqual(ign_off_presence(), 1)

    def test_Digital_IO_presence(self):
        self.assertEqual(digital_io(), 1)

    def test_Analog_IO_presence(self):
        self.assertEqual(analog_io(), 1)


if __name__ == '__main__':
    unittest.main()