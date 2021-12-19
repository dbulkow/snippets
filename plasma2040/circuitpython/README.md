# Example Programs

These instructions will create the environment needed to run the
example programs in this repo. By using CircuitPython, any program
copied to the device will run any time power is provided, not just
when connected to a computer.

This content is summarized from https://learn.pimoroni.com/article/plasma-2040.

# Install

You'll need to copy CircuitPython to the 2040. Grab a copy from
https://circuitpython.org/board/pimoroni_plasma2040/ and drag
to the device mounted as RPI-RP2. The Plasma2040 will restart
and be re-mounted as CIRCUITPY.

These example programs will need some support in the form of library
code. Download the full set from https://circuitpython.org/libraries
and unpack.

Copy the following files and directories to the Plasma2040:

* adafruit_apds9960
* adafruit_bus_device
* adafruit_fancyled
* adafruit_register
* adafruit_rgbled.mpy
* neopixel.mpy
* simpleio.mpy

To run one of the examples, copy the python file to the CIRCUITPY
drive as code.py. When you do this the Plasma2040 will restart and
run your program.
