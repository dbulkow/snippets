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
HUE_3 = 180

# Set up brightness (between 0 and 1)
BRIGHTNESS = 0.2

# Set up speed (wait time between colour changes, in seconds)
SPEED = 0.1

led_strip = neopixel.NeoPixel(board.DATA, NUM_LEDS, brightness=BRIGHTNESS, auto_write=True)

colors = [
    fancy.CHSV(HUE_1 / 360, 1.0, BRIGHTNESS).pack(),
    fancy.CHSV(HUE_2 / 360, 1.0, BRIGHTNESS).pack(),
    fancy.CHSV(HUE_3 / 360, 1.0, BRIGHTNESS).pack(),
]

for i in range(len(led_strip)):
    led_strip[i] = colors[i % 3]

led_strip.show()

idx = 2
while True:
    for i in reversed(range(len(led_strip))):
        led_strip[i] = led_strip[i-1]
        if i == 0:
            led_strip[i] = colors[idx]
        led_strip.show()
        time.sleep(SPEED)

    time.sleep(1)

    idx = (idx - 1) % 3
