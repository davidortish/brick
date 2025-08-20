from abc import ABC, abstractmethod

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor


class RoboDoor(ABC):

    def __init__(
        self,
        hub: InventorHub,
        motor: Motor,
        close_position: int | float,
        is_closed: bool = False,
    ):
        self.hub = hub
        self.motor = motor
        self.close_position = close_position
        self.is_closed = is_closed

    @abstractmethod
    def run(self):
        """Runs the robot"""
        pass

    @abstractmethod
    def open_door(self):
        """Opens the door"""
        pass

    @abstractmethod
    def close_door(self):
        """Closes the door"""
        pass

    @abstractmethod
    def get_status(self) -> bool:
        "Gets the current status of the door (True -> closed, False -> open)"
        pass
