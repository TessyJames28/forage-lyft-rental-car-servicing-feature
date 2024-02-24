import unittest
from datetime import datetime
from car_factory import CarFactory


class TestCreateThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        last_service_mileage = 0
        current_mileage = 20000
        tire_sensor = [0, 1, 0.2, 0.9]
        
        thovex = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(thovex.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 0
        current_mileage = 20000
        tire_sensor = [0, 1, 0.2, 0.9]
        
        thovex = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(thovex.needs_service())
        
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 0
        current_mileage = 30001
        tire_sensor = [0, 1, 0.2, 0.9]
        
        thovex = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(thovex.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 60001
        current_mileage = 80000
        tire_sensor = [0, 1, 0.2, 0.9]
        
        thovex = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(thovex.needs_service())
        
    def test_tire_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 60001
        current_mileage = 80004
        tire_sensor = [1, 1, 0.2, 0.9]
        
        thovex = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(thovex.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 60001
        current_mileage = 80004
        tire_sensor = [1, 0, 0.2, 0.9]
        
        thovex = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(thovex.needs_service())
        
    def test_engine_tire_and_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        last_service_mileage = 60001
        current_mileage = 90004
        tire_sensor = [1, 1, 0.2, 0.9]
        
        thovex = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(thovex.needs_service())
        
    def test_engine_tire_and_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 60001
        current_mileage = 80004
        tire_sensor = [0, 1, 0.2, 0.9]
        
        thovex = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(thovex.needs_service())