# CircuitPython - see https://learn.pimoroni.com/article/plasma-2040
#
# adapted from examples on that page

import board
import adafruit_fancyled.adafruit_fancyled as fancy
import neopixel
import time

# Set how many LEDs you have
NUM_LEDS = 50

# Pick two hues from the colour wheel (from 0-360°, try
# https://www.cssscript.com/demo/hsv-hsl-color-wheel-picker-reinvented/)
HUE_1 = 0
HUE_2 = 127

# Set up brightness (between 0 and 1)
BRIGHTNESS = 0.2

# Set up speed (wait time between colour changes, in seconds)
SPEED = 0.5

led_strip = neopixel.NeoPixel(board.DATA, NUM_LEDS, brightness=BRIGHTNESS, auto_write=True)

while True:
    for i in range(NUM_LEDS):
        # the if statements below use a modulo operation to identify the even and odd numbered LEDs
        if (i % 2) == 0:
            color = fancy.CHSV(HUE_1 / 360, 1.0, BRIGHTNESS)
            # led_strip.set_led(i, color.pack())
            led_strip.fill(color.pack())
        else:
            color = fancy.CHSV(HUE_2 / 360, 1.0, BRIGHTNESS)
            # led_strip.set_led(i, color.pack())
            led_strip.fill(color.pack())
    time.sleep(SPEED)

    for i in range(NUM_LEDS):
        if (i % 2) == 0:
            color = fancy.CHSV(HUE_2 / 360, 1.0, BRIGHTNESS)
            # led_strip.set_led(i, color.pack())
            led_strip.fill(color.pack())
        else:
            color = fancy.CHSV(HUE_1 / 360, 1.0, BRIGHTNESS)
            # led_strip.set_led(i, color.pack())
            led_strip.fill(color.pack())
    time.sleep(SPEED)
