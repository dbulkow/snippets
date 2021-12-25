# This super simple example sets up two alternating colours, great for festive lights!

import board
import adafruit_fancyled.adafruit_fancyled as fancy
import neopixel
import time

# Set how many LEDs you have
NUM_LEDS = 50

# Pick two hues from the colour wheel (from 0-360°, try https://www.cssscript.com/demo/hsv-hsl-color-wheel-picker-reinvented/ )
HUE_1 = 0
HUE_2 = 127

# Set up brightness (between 0 and 1)
BRIGHTNESS = 0.2

# Set up speed (wait time between colour changes, in seconds)
SPEED = 0.2

led_strip = neopixel.NeoPixel(board.DATA, NUM_LEDS, brightness=BRIGHTNESS, auto_write=True)

led_strip.fill(fancy.CHSV(HUE_2 / 360, 1.0, BRIGHTNESS).pack())

while True:
    for i in range(len(led_strip)):
        color = fancy.CHSV(HUE_1 / 360, 1.0, BRIGHTNESS)
        led_strip[i] = color.pack()
        led_strip.show()
        time.sleep(SPEED)

    for i in reversed(range(len(led_strip))):
        color = fancy.CHSV(HUE_2 / 360, 1.0, BRIGHTNESS)
        led_strip[i] = color.pack()
        led_strip.show()
        time.sleep(SPEED)
