import logging

from pybricks.hubs import InventorHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor

from robo_door import RoboDoor


class DoorController(RoboDoor):
    def __init__(self):
        super().__init__(
            InventorHub(),
            Motor(Port.A, Direction.COUNTERCLOCKWISE),
            130, 1000, 1000
        )
        logging.basicConfig(
            filename="door_actions.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def open_door(self):
        try:
            logging.info("Opening door.")
            self.motor.run_target(self.open_speed, 0, wait=True)
            logging.info("Door opened (motor at angle 0).")
            super().open_door()
        except Exception as e:
            logging.error(f"Error opening door: {e}")

    def close_door(self):
        try:
            logging.info(f"Closing door to position {self.close_position}.")
            self.motor.run_target(self.close_speed, self.close_position, wait=True)
            logging.info("Door closed.")
            super().close_door()
        except Exception as e:
            logging.error(f"Error closing door: {e}")

    @staticmethod
    def clean_log():
        with open("door_actions.log", "w"):
            pass

    @staticmethod
    def get_log():
        with open("door_actions.log", "r") as f:
            return f.read()
        
def test():
    # init door
    door = DoorController()
    
    # clean log
    door.clean_log()
    
    # open door
    door.open_door()

    # close door
    door.close_door()
    
    # check status
    print(door.get_status())

if __name__ == "__main__":
    test()
