from abc import ABC


class Battery(ABC):
    def needs_service(self):
        return True if True else False
