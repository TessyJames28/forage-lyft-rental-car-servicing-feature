import unittest
from engine.capulet_engine import CapuletEngine
        
        
class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 30001
        
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(capulet_engine.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        last_service_mileage = 30001
        current_mileage = 50000
        
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(capulet_engine.needs_service())
        