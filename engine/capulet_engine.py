from engine.engine import Engine


# Capulet Engine needs servicing once every 30,000 miles
class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        super().__init__()
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        
        
    def needs_service(self):
        milleage = self.current_mileage - self.last_service_mileage
        return milleage > 30000