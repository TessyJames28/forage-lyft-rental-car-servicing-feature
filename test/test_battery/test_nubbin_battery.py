import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_serviced_date = today.replace(year=today.year - 5)
        
        nubbin_battery = NubbinBattery(last_serviced_date, today)
        self.assertTrue(nubbin_battery.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_serviced_date = today.replace(year=today.year - 3)
        
        nubbin_battery = NubbinBattery(last_serviced_date, today)
        self.assertFalse(nubbin_battery.needs_service())
        
