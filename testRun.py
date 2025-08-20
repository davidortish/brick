import os

import keyboard

while True:
    if keyboard.is_pressed("q"):
        os.system("pybricksdev run ble product_test.py")
