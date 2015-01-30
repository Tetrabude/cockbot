'''
Created on 30.01.2015

@author: peter
'''
import unittest
import time
from hardware.PumpControl import PumpControl
from hardware.PumpControlMock import PumpControlMock


class TestPumpControlMock(unittest.TestCase):
    

    def setUp(self):
        self.pumpA = PumpControlMock(25)


    def tearDown(self):
        pass


    def test_runPump(self):
        self.assertTrue(self.pumpA.runPump(1), "Pump failes")
        
    def test_runPumpAsync(self):
        waitTime = 5
        startTime = time.time()
        self.pumpA.runPumpAsync(waitTime)
        self.pumpA.join()
        duration = time.time() - startTime
        
        
        self.assertTrue(duration >= waitTime , "Pump cycle to short")
        self.assertTrue(duration <= waitTime + 1 , "Pump cycle to long")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()