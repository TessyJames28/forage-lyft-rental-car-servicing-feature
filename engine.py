class Engine:
    def needs_service(self):
        return True if True else False
    

# Capulet Engine needs servicing once every 30,000 miles
class CapuletEngine(Engine):
    def __init__(self, last_service_milleage, current_milleage):
        super().__init__()
        self.last_service_milleage = last_service_milleage
        self.current_milleage = current_milleage
        
        
    def needs_servicing(self):
        total_milleage = self.last_service_milleage + self.current_milleage
        return total_milleage >= 30000


# Willoughby Engine needs servicing once every 60,000 miles
class WilloughbyEngine(Engine):
    def __init__(self, last_service_milleage, current_milleage):
        super().__init__()
        self.last_service_milleage = last_service_milleage
        self.current_milleage = current_milleage
        
        
    def needs_servicing(self):
        total_milleage = self.last_service_milleage + self.current_milleage
        return total_milleage >= 60000



# Sternman Engine needs sercing only when the warning indicator is on
class SternmanEngine(Engine):
    def __init__(self, warning_light_on):
        super().__init__()
        self.warning_light_on = warning_light_on
        
        
    def needs_servicing(self):
        return self.warning_light_on