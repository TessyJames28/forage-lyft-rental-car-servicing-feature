from datetime import timedelta
class Battery:
    def needs_service(self):
        return True if True else False
    


# Spindler Battery needs servicing once every 2 years
class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date
        
        
    def needs_service(self):
        service_interval = timedelta(days=365 * 2)
        last_serviced = self.current_date - self.last_service_date
        return last_serviced >= service_interval


# Nubbin Battery needs servicing once every 4 years
class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date
        
        
    def needs_service(self):
        service_interval = timedelta(days=365 * 4)
        last_serviced = self.current_date - self.last_service_date
        return last_serviced >= service_interval