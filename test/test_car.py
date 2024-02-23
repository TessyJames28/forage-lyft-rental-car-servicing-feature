import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from car_factory import CarFactory


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
        
        
class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_serviced_date = today.replace(year=today.year - 3)
        
        spindler_battery = SpindlerBattery(last_serviced_date, today)
        self.assertTrue(spindler_battery.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_serviced_date = today.replace(year=today.year - 1)
        
        spindler_battery = SpindlerBattery(last_serviced_date, today)
        self.assertFalse(spindler_battery.needs_service())
        
        
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
        
        
class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_on = True
        
        sternman_engine = SternmanEngine(warning_light_on)
        self.assertTrue(sternman_engine.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        warning_light_on = False
        
        sternman_engine = SternmanEngine(warning_light_on)
        self.assertFalse(sternman_engine.needs_service())


# Test each of the car model

class TestCreateCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 0
        current_mileage = 20000
        
        calliope = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(calliope.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 0
        current_mileage = 20000
        
        calliope = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(calliope.needs_service())
        
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 0
        current_mileage = 30001
        
        calliope = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(calliope.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 30001
        current_mileage = 50000
        
        calliope = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(calliope.needs_service())
        
    def test_engine_and_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 30001
        current_mileage = 60004
        
        calliope = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(calliope.needs_service())
        
    def test_engine_and_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 30001
        current_mileage = 50004
        
        calliope = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(calliope.needs_service())
        
        
class TestCreateGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        last_service_mileage = 0
        current_mileage = 20000
        
        glissade = CarFactory.create_glissade(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(glissade.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 0
        current_mileage = 20000
        
        glissade = CarFactory.create_glissade(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(glissade.needs_service())
        
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 0
        current_mileage = 60001
        
        glissade = CarFactory.create_glissade(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(glissade.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 60001
        current_mileage = 110000
        
        glissade = CarFactory.create_glissade(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(glissade.needs_service())
        
    def test_engine_and_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        last_service_mileage = 60001
        current_mileage = 120004
        
        glissade = CarFactory.create_glissade(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(glissade.needs_service())
        
    def test_engine_and_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 60001
        current_mileage = 110004
        
        glissade = CarFactory.create_glissade(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(glissade.needs_service())


class TestCreatePalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_on = False
        
        palindrome = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on)
        self.assertTrue(palindrome.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_on = False
        
        palindrome = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on)
        self.assertFalse(palindrome.needs_service())
        
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_on = True
        
        palindrome = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on)
        self.assertTrue(palindrome.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_on = False
        
        palindrome = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on)
        self.assertFalse(palindrome.needs_service())
        
    def test_engine_and_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_on = True
        
        palindrome = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on)
        self.assertTrue(palindrome.needs_service())
        
    def test_engine_and_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_on = False
        
        palindrome = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on)
        self.assertFalse(palindrome.needs_service())


class TestCreateRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        last_service_mileage = 0
        current_mileage = 20000
        
        rorschach = CarFactory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(rorschach.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 0
        current_mileage = 20000
        
        rorschach = CarFactory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(rorschach.needs_service())
        
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 0
        current_mileage = 60001
        
        rorschach = CarFactory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(rorschach.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 60001
        current_mileage = 110000
        
        rorschach = CarFactory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(rorschach.needs_service())
        
    def test_engine_and_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        last_service_mileage = 60001
        current_mileage = 120004
        
        rorschach = CarFactory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(rorschach.needs_service())
        
    def test_engine_and_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 60001
        current_mileage = 120000
        
        rorschach = CarFactory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(rorschach.needs_service())


class TestCreateThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        last_service_mileage = 0
        current_mileage = 20000
        
        thovex = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(thovex.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 0
        current_mileage = 20000
        
        thovex = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(thovex.needs_service())
        
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 0
        current_mileage = 30001
        
        thovex = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(thovex.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 60001
        current_mileage = 80000
        
        thovex = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(thovex.needs_service())
        
    def test_engine_and_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        last_service_mileage = 60001
        current_mileage = 90004
        
        thovex = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(thovex.needs_service())
        
    def test_engine_and_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 60001
        current_mileage = 80004
        
        thovex = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(thovex.needs_service())
