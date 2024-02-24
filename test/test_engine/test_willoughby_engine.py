import unittest
from engine.willoughby_engine import WilloughbyEngine
        
        
class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 60001
        
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(willoughby_engine.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        last_service_mileage = 60001
        current_mileage = 110000
        
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(willoughby_engine.needs_service())
        
