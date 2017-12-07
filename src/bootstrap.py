#!/usr/bin/python

"""
use "from bootstrap import *" from any script to do all the standard setup 
and checks needed by any script
"""

from time import sleep
from neopixel import *

import os.path
import sys

# Check that the system is set up like we want it
dev = '/dev/spidev0.0'

if not os.path.exists(dev):
    sys.stderr.write("""
The SPI device /dev/spidev0.0 does not exist. You may need to load
the appropriate kernel modules. Try:
sudo modprobe spi_bcm2708 ; sudo modprobe spidev
You may also need to unblacklist the spi_bcm2708 module in 
/etc/modprobe.d/raspi-blacklist.conf
""")
    sys.exit(2)

#permissions check
try:
    open(dev)
except IOError as  e:
    if e.errno == 13:
        sys.stderr.write("""
It looks like SPI device /dev/spidev0.0 has the wrong permissions.
Try making it world writable:
sudo chmod a+rw /dev/spidev0.0
""")
    sys.exit(2)

# good configurations for ws2811 and SPI
# LED strip configuration:
LED_COUNT      = 49      # Number of LED pixels.
LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
# Intialize the library (must be called once before other functions).
strip.begin()
