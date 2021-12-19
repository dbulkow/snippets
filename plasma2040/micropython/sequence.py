# Micropython - see https://learn.pimoroni.com/article/plasma-2040
#
# adapted from examples on that page

import plasma
from plasma import plasma2040
import time

NUM_LEDS = 50

led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma2040.DAT)

led_strip.start()
while True:
    for i in range(NUM_LEDS):
        led_strip.set_rgb(i, 255, 0, 0)
        time.sleep(0.25)
        led_strip.set_rgb(i, 0, 0, 0)

