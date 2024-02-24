import unittest
from datetime import datetime
from car_factory import CarFactory

class TestCreateCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        last_service_mileage = 0
        current_mileage = 20000
        tire_sensor = [0, 1, 0.2, 0.9]
        
        calliope = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(calliope.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 0
        current_mileage = 20000
        tire_sensor = [0, 1, 0.2, 0.9]
        
        calliope = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(calliope.needs_service())
        
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 0
        current_mileage = 30001
        tire_sensor = [0, 1, 0.2, 0.9]
        
        calliope = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(calliope.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 30001
        current_mileage = 50000
        tire_sensor = [0, 1, 0.2, 0.9]
        
        calliope = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(calliope.needs_service())
        
    def test_tire_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 30001
        current_mileage = 50000
        tire_sensor = [1, 1, 0.2, 0.9]
        
        calliope = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(calliope.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 30001
        current_mileage = 50000
        tire_sensor = [1, 1, 0.2, 0.7]
        
        calliope = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(calliope.needs_service())
        
    def test_engine_tire_and_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 30001
        current_mileage = 60004
        tire_sensor = [1, 0.9, 0.8, 0.7]
        
        calliope = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(calliope.needs_service())
        
    def test_engine_tire_and_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 30001
        current_mileage = 50004
        tire_sensor = [0.2, 0.9, 0.8, 0.7]
        
        calliope = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(calliope.needs_service())
        
