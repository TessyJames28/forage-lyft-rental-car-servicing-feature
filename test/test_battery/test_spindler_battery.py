import unittest
from datetime import datetime
from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_serviced_date = today.replace(year=today.year - 4)
        
        spindler_battery = SpindlerBattery(last_serviced_date, today)
        self.assertTrue(spindler_battery.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_serviced_date = today.replace(year=today.year - 1)
        
        spindler_battery = SpindlerBattery(last_serviced_date, today)
        self.assertFalse(spindler_battery.needs_service())
        
