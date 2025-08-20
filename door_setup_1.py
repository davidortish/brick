from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

from robo_door import RoboDoor


class DoorSetup1(RoboDoor):
    def __init__(self):
        super().__init__(InventorHub(), Motor(Port.A, Direction.COUNTERCLOCKWISE), 130)

    def run(self):
        self.motor.reset_angle(0)

        while True:
            if Button.LEFT in self.hub.buttons.pressed():
                if not self.is_closed:
                    self.close_door()
                else:
                    self.open_door()

                # Debounce
                while Button.LEFT in self.hub.buttons.pressed():

                    wait(10)
            wait(10)  # Prevent busy-waiting

    def open_door(self):
        self.motor.run_target(1000, 0, wait=True)
        super().open_door()

    def close_door(self):
        self.motor.run_target(1000, self.close_position, wait=True)
        super().close_door()


if __name__ == "__main__":
    door = DoorSetup1()
    # door.run()
