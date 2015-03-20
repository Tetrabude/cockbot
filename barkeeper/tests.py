from django.test import TestCase
from barkeeper.models import Pump



class barkeeperTests(TestCase):
    
    
    
    def setUp(self):
        Pump.objects.create(name="PumpA", gpioId=5, mlPerMin=40.0)

    def test_pump_can_be_accessed(self):
        pumpA = Pump.objects.get(name="PumpA")
        self.assertEqual(pumpA.name, "PumpA", "Name of pump not correct")
        self.assertEqual(pumpA.gpioId, 5, "GPIOID of pump not correct")
        self.assertEqual(pumpA.mlPerMin, 40.0, "Milliliter per Minute not correct")
        
        unic = pumpA.name + " " + str(pumpA.gpioId) + " " + str(pumpA.mlPerMin)
        self.assertEqual(unic, str(pumpA), "Unicodemethod not Correct")