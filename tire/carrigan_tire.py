from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_sensor):
        self.tire_sensor = tire_sensor
        
        
    def needs_service(self):
        for val in self.tire_sensor:
            if val >= 0.9:
                return True
        return False 