import unittest
from datetime import datetime
from car_factory import CarFactory


class TestCreateRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        last_service_mileage = 0
        current_mileage = 20000
        tire_sensor = [0, 0.8, 0.2, 0.6]
        
        rorschach = CarFactory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(rorschach.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 0
        current_mileage = 20000
        tire_sensor = [0, 0.8, 0.2, 0.6]
        
        rorschach = CarFactory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(rorschach.needs_service())
        
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 0
        current_mileage = 60001
        tire_sensor = [0, 0.8, 0.2, 0.6]
        
        rorschach = CarFactory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(rorschach.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 60001
        current_mileage = 110000
        tire_sensor = [0, 0.8, 0.2, 0.6]
        
        rorschach = CarFactory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(rorschach.needs_service())
        
    def test_tire_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 60001
        current_mileage = 110004
        tire_sensor = [0.6, 0.8, 0.9, 0.6]
        
        rorschach = CarFactory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(rorschach.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 60001
        current_mileage = 110004
        tire_sensor = [0.6, 0.8, 0.4, 0.6]
        
        rorschach = CarFactory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(rorschach.needs_service())
        
    def test_engine_tire_and_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        last_service_mileage = 60001
        current_mileage = 120004
        tire_sensor = [0.6, 0.8, 0.9, 0.6]
        
        rorschach = CarFactory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(rorschach.needs_service())
        
    def test_engine_tire_and_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 60001
        current_mileage = 120000
        tire_sensor = [0, 0.8, 0.2, 0.6]
        
        rorschach = CarFactory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(rorschach.needs_service())
