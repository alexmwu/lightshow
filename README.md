# lightshow
Uses AWS Greengrass and Raspberry Pi to demonstrate concepts for an LED light show (uses lightshowpi)
Only demos ws2811 LEDs

## External Libraries
Install these libraries first:

* rpi_ws281x (based on commit 7f08d491f0ae22c20a63394df6a5c8ebe80c0be4)
* lightshowpi (based on commit 567881439adfcc5dad5c7150fefaef249942114f)

## Hardware
* RPi model 3
* 5V power supply with enough amps to power LED strip (e.g., for 50, need 3A. 100, 6A)
* breadboard friendly 2.1mm DC barrel jack (female)
* jack adaptor
* 3.3 to 5V lvl shifter
* breadboard
* jumper wires
* ws2811 LEDs

### optional
* resistors
* LEDs
* T breakout board with 40 pin RPi GPIO cable

## Directory Structure
* /config
    * example config for lightshowpi. diff with the defaults to see changes
* /examples
    * example file for testing if the rpi lib is working; adjusted for ws2811
* /src
    * files for use with lightshowpi
    * synchronized_lights_led_strip.py is the most important for getting the show going
    * bootstrap.py sets up variables
    * /lambda
        * lambdas to trigger some useful actions for the show (fetching prefs, playing show on Greengrass core)
    * /ggDevice
        * creates an example greengrass aware device using the gg SDK
* /tutorials
    * get started with RPi GPIO

* /examples
    * example test file for running rpi_ws281x
* /config
    * config for lightshowpi

## Gotchas
* when in doubt, deploy to the gg core
* remember to include __init__.py if you want to use synchronized_lights_led_strip.py as a library
* ensure Greengrass has local resource access
* set the SYNCHRONIZED_LIGHTS_HOME env variable to the lightshowpi install directory in your lambda function
* remember to use chgrp, chmod, chown to fix docker permissions issues
* reinstall lightshowpi (install.sh) to fix environment issues
