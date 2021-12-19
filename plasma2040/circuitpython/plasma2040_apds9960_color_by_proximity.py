# CircuitPython - see https://learn.pimoroni.com/article/plasma-2040
#
# adapted from examples on that page

import board
import busio
import adafruit_apds9960.apds9960
import adafruit_rgbled
import neopixel
import time

NUM_LEDS = 50

BRIGHTNESS = 1

led_strip = neopixel.NeoPixel(board.DATA, NUM_LEDS, brightness=BRIGHTNESS, auto_write=True)

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True

led = adafruit_rgbled.RGBLED(board.LED_R, board.LED_G, board.LED_B, invert_pwm = True)

while True:
    led_strip.fill((sensor.proximity, 0, 0))
    time.sleep(0.2)
