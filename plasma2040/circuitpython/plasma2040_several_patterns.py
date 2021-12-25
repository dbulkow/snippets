# This super simple example sets up two alternating colours, great for festive lights!

import board
import adafruit_fancyled.adafruit_fancyled as fancy
import neopixel
import time

# Set how many LEDs you have
NUM_LEDS = 50

# Set up brightness (between 0 and 1)
BRIGHTNESS = 0.35

# Set up speed (wait time between colour changes, in seconds)
SPEED = 0.1
FAST_SPEED = 0.05

led_strip = neopixel.NeoPixel(board.DATA, NUM_LEDS, brightness=BRIGHTNESS, auto_write=True)

# Pick two hues from the colour wheel (from 0-360°, try https://www.cssscript.com/demo/hsv-hsl-color-wheel-picker-reinvented/ )
HUE_1 = 0
HUE_2 = 127
HUE_3 = 180

colors = [
    fancy.CHSV(HUE_1 / 360, 1.0, BRIGHTNESS).pack(),
    fancy.CHSV(HUE_2 / 360, 1.0, BRIGHTNESS).pack(),
    fancy.CHSV(HUE_3 / 360, 1.0, BRIGHTNESS).pack(),
]

red = colors[0]
green = colors[1]
blue = colors[2]

pattern = [0] * (NUM_LEDS + 10)
idx = 0
for i in range(len(pattern)):
    pattern[i] = colors[idx]
    if (i > 0) and ((i % 5) == 0):
        idx = (idx + 1) % 3

while True:
    # marching color change

    start = time.time()

    for i in range(len(led_strip)):
        led_strip[i] = colors[i % 3]
        led_strip.show()
        time.sleep(FAST_SPEED)

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

        elapsed = time.time() - start
        if elapsed > (2 * 60):
            break

    # red chases green back and forth

    start = time.time()

    while True:
        for i in range(len(led_strip)):
            led_strip[i] = red
            led_strip.show()
            time.sleep(SPEED)

        for i in reversed(range(len(led_strip))):
            led_strip[i] = green
            led_strip.show()
            time.sleep(SPEED)

        elapsed = time.time() - start
        if elapsed > (2 * 60):
            break

    # multi-color transition

    start = time.time()

    for i in range(len(led_strip)):
        led_strip[i] = colors[i % 3]
        led_strip.show()
        time.sleep(FAST_SPEED)

    for i in range(len(led_strip)):
        led_strip[i] = 0
        led_strip.show()
        time.sleep(FAST_SPEED)

    # red replaces green

    start = time.time()

    while True:
        for i in range(len(led_strip)):
            led_strip[i] = red
            led_strip.show()
            time.sleep(SPEED)

        for i in range(len(led_strip)):
            led_strip[i] = green
            led_strip.show()
            time.sleep(SPEED)

        elapsed = time.time() - start
        if elapsed > (2 * 60):
            break

    # red runner back and forth

    start = time.time()

    while True:
        for i in range(len(led_strip)-1):
            led_strip[i] = red
            led_strip[i+1] = red
            led_strip.show()
            time.sleep(SPEED)
            led_strip[i] = green
            led_strip.show()
            time.sleep(FAST_SPEED)

        for i in reversed(range(len(led_strip)-1)):
            led_strip[i] = red
            led_strip[i+1] = red
            led_strip.show()
            time.sleep(SPEED)
            led_strip[i+1] = green
            led_strip.show()
            time.sleep(FAST_SPEED)

        elapsed = time.time() - start
        if elapsed > (45):
            break

    # rolling pattern

    start = time.time()

    while True:
        for ii in range(len(pattern)):
            for i in range(len(led_strip)):
                led_strip[i] = pattern[(i + ii) % len(pattern)]
            led_strip.show()
            time.sleep(SPEED)

        elapsed = time.time() - start
        if elapsed > (2 * 60):
            break

    for i in reversed(range(len(led_strip))):
        led_strip[i] = 0
        led_strip.show()
        time.sleep(SPEED)
