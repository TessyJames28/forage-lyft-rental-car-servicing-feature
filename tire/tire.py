from abc import ABC


class Tire(ABC):
    def needs_service(self):
        return True if True else False 