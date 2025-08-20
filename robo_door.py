from abc import ABC, abstractmethod

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor


class RoboDoor(ABC):

    def __init__(
        self,
        hub: InventorHub,
        motor: Motor,
        close_position: int | float,
        close_speed: int | float,
        open_speed: int | float,
        is_closed: bool = False,
    ):
        self.hub = hub
        self.motor = motor
        self.close_position = close_position
        self.close_speed = close_speed
        self.open_speed = open_speed
        self.is_closed = is_closed

    @abstractmethod
    def open_door(self):
        """Opens the door"""
        self.is_closed = False

    @abstractmethod
    def close_door(self):
        """Closes the door"""
        self.is_closed = True

    def get_status(self) -> str:
        "Gets the current status of the door (True -> closed, False -> open)"
        return "closed" if self.is_closed else "open"

    def set_status(self, is_closed: bool):
        self.is_closed = is_closed
