# CircuitPython - see https://learn.pimoroni.com/article/plasma-2040
#
# adapted from examples on that page

import board
import digitalio
import adafruit_rgbled
import neopixel

NUM_LEDS = 50

BRIGHTNESS = 1

led_strip = neopixel.NeoPixel(board.DATA, NUM_LEDS, brightness=BRIGHTNESS, auto_write=True)

button_boot = digitalio.DigitalInOut(board.USER_SW)
button_boot.direction = digitalio.Direction.INPUT
button_boot.pull = digitalio.Pull.UP

button_a = digitalio.DigitalInOut(board.SW_A)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.UP

button_b = digitalio.DigitalInOut(board.SW_B)
button_b.direction = digitalio.Direction.INPUT
button_b.pull = digitalio.Pull.UP

led = adafruit_rgbled.RGBLED(board.LED_R, board.LED_G, board.LED_B, invert_pwm = True)

def button_read(button):
    return not button.value

while True:
    if button_read(button_a):
        led_strip.fill((255, 0, 0))
        led.color = (255, 0, 0)
    if button_read(button_b):
        led_strip.fill((0, 255, 0))
        led.color = (0, 255, 0)
    if button_read(button_boot):
        led_strip.fill((0, 0, 0))
        led.color = (0, 0, 0)
