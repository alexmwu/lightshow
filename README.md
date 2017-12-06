# lightshow
Uses AWS Greengrass and Raspberry Pi to demonstrate concepts for an LED light show (uses lightshowpi)
Only demos ws2811 LEDs

## External Libraries
Install these libraries first
rpi_ws281x (based on commit 7f08d491f0ae22c20a63394df6a5c8ebe80c0be4)
lightshowpi (based on commit 567881439adfcc5dad5c7150fefaef249942114f)

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
* /tutorials
** get started with RPi GPIO
* /src
** files for use with lightshowpi
* /examples
** example test file for running rpi_ws281x
* /config
** config for lightshowpi
