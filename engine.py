class Engine:
    def needs_service(self):
        return True if True else False
    

# Capulet Engine needs servicing once every 30,000 miles
class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        super().__init__()
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        
        
    def needs_servicing(self):
        milleage = self.current_mileage - self.last_service_mileage
        return milleage >= 30000


# Willoughby Engine needs servicing once every 60,000 miles
class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        super().__init__()
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        
        
    def needs_servicing(self):
        milleage = self.current_mileage - self.last_service_mileage
        return milleage >= 60000



# Sternman Engine needs sercing only when the warning indicator is on
class SternmanEngine(Engine):
    def __init__(self, warning_light_on):
        super().__init__()
        self.warning_light_on = warning_light_on
        
        
    def needs_servicing(self):
        return self.warning_light_on