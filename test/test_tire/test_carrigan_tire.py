import unittest
from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_sensor = [1, 0.9, 0.2, 0.7]
        
        carrigan_tire = CarriganTire(tire_sensor)
        self.assertTrue(carrigan_tire.needs_service())
        
        
    def test_tire_should_be_serviced_with_one_occurrence(self):
        tire_sensor = [0.4, 0.9, 0.2, 0.7]
        
        carrigan_tire = CarriganTire(tire_sensor)
        self.assertTrue(carrigan_tire.needs_service())
        
        
    def test_tire_should_not_be_serviced(self):
        tire_sensor = [0.3, 0.8, 0.5, 0.4]
        
        carrigan_tire = CarriganTire(tire_sensor)
        self.assertFalse(carrigan_tire.needs_service())