from engine.engine import Engine


# Willoughby Engine needs servicing once every 60,000 miles
class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        super().__init__()
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        
        
    def needs_servicing(self):
        milleage = self.current_mileage - self.last_service_mileage
        return milleage >= 60000