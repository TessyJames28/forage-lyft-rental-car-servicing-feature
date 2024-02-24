import unittest
from tire.octoprime_tire import OctoPrimeTire


class TestOctoPrimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_sensor = [1, 0.9, 0.2, 1]
        
        octoprime_tire = OctoPrimeTire(tire_sensor)
        self.assertTrue(octoprime_tire.needs_service())
        
        
    def test_tire_should_not_be_serviced(self):
        tire_sensor = [1, 0.9, 0.2, 0.8]
        
        octoprime_tire = OctoPrimeTire(tire_sensor)
        self.assertFalse(octoprime_tire.needs_service())
        