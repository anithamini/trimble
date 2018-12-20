from source.HMP import *
from source.AlertTest import *
from source.PVT import *
import unittest

class suiteTest(unittest.TestCase):
    def setUpClass(cls):
        print("Running the suite")

    def tearDownClass(cls):
        print("Ending the suite")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(HMPsuite,Alertsuite,PVTsuite))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    result=runner.run(test_suite)
    print("---- START OF TEST RESULTS")
    print(result)

    print("result::errors")
    print(result.errors)

    print("result::failures")
    print(result.failures)

    print("result::skipped")
    print(result.skipped)

    print("result::successful")
    print(result.wasSuccessful())

    print("result::test-run")
    print(result.testsRun)