from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

hub = InventorHub()
motorRight = Motor(Port.A, Direction.COUNTERCLOCKWISE)
# flipped


motorRight.reset_angle(0)

CLOSE_POSITION = 130
is_closed = False


while True:
    if Button.LEFT in hub.buttons.pressed():
        if not is_closed:
            # Close

            motorRight.run_target(1000, CLOSE_POSITION, wait=True)
            is_closed = True
        else:
            # Open

            motorRight.run_target(1000, 0, wait=True)
            is_closed = False

        # Debounce
        while Button.LEFT in hub.buttons.pressed():

            wait(10)
    print(motorRight.angle())
    wait(10)  # Prevent busy-waiting
