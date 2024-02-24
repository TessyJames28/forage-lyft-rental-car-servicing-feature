import unittest
from datetime import datetime
from car_factory import CarFactory

class TestCreatePalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        warning_light_on = False
        tire_sensor = [0.6, 0.8, 0.4, 0.6]
        
        palindrome = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on, tire_sensor)
        self.assertTrue(palindrome.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_on = False
        tire_sensor = [0.6, 0.8, 0.4, 0.6]
        
        palindrome = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on, tire_sensor)
        self.assertFalse(palindrome.needs_service())
        
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_on = True
        tire_sensor = [0.6, 0.8, 0.4, 0.6]
        
        palindrome = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on, tire_sensor)
        self.assertTrue(palindrome.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_on = False
        tire_sensor = [0.6, 0.8, 0.4, 0.6]
        
        palindrome = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on, tire_sensor)
        self.assertFalse(palindrome.needs_service())
        
    def test_tire_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_on = True
        tire_sensor = [0.6, 0.9, 0.4, 0.6]
        
        palindrome = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on, tire_sensor)
        self.assertTrue(palindrome.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_on = False
        tire_sensor = [0.6, 0.8, 0.4, 0.6]
        
        palindrome = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on, tire_sensor)
        self.assertFalse(palindrome.needs_service())
        
    def test_engine_tire_and_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_on = True
        tire_sensor = [0.6, 0.9, 0.4, 0.6]
        
        palindrome = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on, tire_sensor)
        self.assertTrue(palindrome.needs_service())
        
    def test_engine_tire_and_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_on = False
        tire_sensor = [0.6, 0.8, 0.4, 0.6]
        
        palindrome = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on, tire_sensor)
        self.assertFalse(palindrome.needs_service())
