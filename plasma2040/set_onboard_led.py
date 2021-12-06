# Micropython - see https://learn.pimoroni.com/article/plasma-2040
#
# adapted from examples on that page

from plasma import plasma2040
from pimoroni import RGBLED

led = RGBLED(plasma2040.LED_R, plasma2040.LED_G, plasma2040.LED_B)

led.set_rgb(255, 0, 0)
