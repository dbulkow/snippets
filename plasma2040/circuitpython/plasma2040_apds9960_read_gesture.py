# CircuitPython - see https://learn.pimoroni.com/article/plasma-2040
#
# adapted from examples on that page

import board
import busio
import adafruit_apds9960.apds9960
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_gesture = True
sensor.enable_proximity = True

direction = [
    'none',
    'up',
    'down',
    'left',
    'right',
]

print('ready for gestures')

while True:
    gesture = sensor.gesture()
    if gesture != 0:
        print('Saw gesture: {0}'.format(direction[gesture]))
    time.sleep(0.2)
