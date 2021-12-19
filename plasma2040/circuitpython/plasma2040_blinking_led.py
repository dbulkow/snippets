# CircuitPython - see https://learn.pimoroni.com/article/plasma-2040
#
# adapted from examples on that page

import board
import adafruit_rgbled
import time

led = adafruit_rgbled.RGBLED(board.LED_R, board.LED_G, board.LED_B, invert_pwm = True)

while True:
    led.color = (127, 0, 0)
    time.sleep(0.2)
    led.color = (64, 0, 0)
    time.sleep(1)
