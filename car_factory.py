# Cars are created by calling the corresponding CarFactory
from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine


class CarFactory:
    
    # creates the model Calliope that has Capulet Engine and Spindler Battery
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        # create instances for Capulet engine and Spindler battery
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        
        # creates a car instances using engine and battery
        calliope = Car(engine, battery)
        return calliope
    
    
    # creates Glissade model that uses Willoughby Engine and Spindler Battery
    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        # create instances for Willoughby engine and Spindler battery
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        
        # creates a car instances using engine and battery
        glissade = Car(engine, battery)
        return glissade
    
    
    
    # create Palindrome model that uses Sternman Engine and Spindler Battery
    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        # create instances for Sternman engine and Spindler battery
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        
        # creates a car instances using engine and battery
        palindrome = Car(engine, battery)
        return palindrome
    
    
    
    # create Rorschach model that uses Willoughby Engine and Nubbin Battery
    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        # create instances for Willoughby engine and Nubbin battery
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        
        # creates a car instances using engine and battery
        rorschach = Car(engine, battery)
        return rorschach
    
    
    
    # create Thovex model that uses Capulet Engine and Nubbin Battery
    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        # create instances for Capulet engine and Nubbin battery
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        
        # creates a car instances using engine and battery
        thovex = Car(engine, battery)
        return thovex
        