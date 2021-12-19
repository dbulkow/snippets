# Micropython - see https://learn.pimoroni.com/article/plasma-2040
#
# adapted from examples on that page

import plasma
from plasma import plasma2040
from pimoroni import RGBLED, Button

NUM_LEDS = 50

led = RGBLED(plasma2040.LED_R, plasma2040.LED_G, plasma2040.LED_B)
led.set_rgb(0, 0, 0)

button_a = Button(plasma2040.BUTTON_A)
button_b = Button(plasma2040.BUTTON_B)
button_boot = Button(plasma2040.USER_SW)

led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma2040.DAT)

led_strip.start()

while True:
    if button_a.read():
        for i in range(NUM_LEDS):
            led_strip.set_rgb(i, 255, 0, 0)
        led.set_rgb(255, 0, 0)
    if button_b.read():
        for i in range(NUM_LEDS):
            led_strip.set_rgb(i, 0, 255, 0)
        led.set_rgb(0, 255, 0)
    if button_boot.read():
        for i in range(NUM_LEDS):
            led_strip.set_rgb(i, 0, 0, 0)
        led.set_rgb(0, 0, 0)

