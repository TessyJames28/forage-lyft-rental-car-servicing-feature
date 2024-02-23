from datetime import timedelta
from battery.battery import Battery


# Nubbin Battery needs servicing once every 4 years
class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date
        
        
    def needs_service(self):
        service_interval = timedelta(days=365 * 4)
        last_serviced = self.current_date - self.last_service_date
        return last_serviced > service_interval