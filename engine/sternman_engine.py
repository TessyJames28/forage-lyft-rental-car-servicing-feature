from engine.engine import Engine


# Sternman Engine needs sercing only when the warning indicator is on
class SternmanEngine(Engine):
    def __init__(self, warning_light_on):
        super().__init__()
        self.warning_light_on = warning_light_on
        
        
    def needs_service(self):
        return self.warning_light_on