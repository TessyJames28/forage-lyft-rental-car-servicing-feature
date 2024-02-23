# An interface to access cars
from abc import ABC, abstractmethod

class Serviceable(ABC):
    
    @abstractmethod
    def needs_service(self):
        pass
        