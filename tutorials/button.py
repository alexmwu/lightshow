import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

# Pin 19 will sense for button pushing
button = 19
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# The LED
led = 21
GPIO.setup(led, GPIO.OUT)

loops = 0

try:
    while True:
        input_state = GPIO.input(button) # Sense the button
        if input_state == False:
            loops += 1
            sys.stdout.write('\r')
            sys.stdout.flush()
            sys.stdout.write('Button Pressed; loops = ' + str(loops))
            # time.sleep(0.2)
            # Switch on LED
            GPIO.output(led, 1)
        else :
            # Switch off LED
            GPIO.output(led, 0)
            loops = 0
except KeyboardInterrupt:
    GPIO.cleanup()

