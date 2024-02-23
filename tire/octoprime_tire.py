from tire.tire import Tire


class OctoPrimeTire(Tire):
    def __init__(self, tire_sensor):
        self.tire_sensor = tire_sensor
        
        
    def needs_service(self):
        
        total= sum(self.tire_sensor)
        return total >= 3
            