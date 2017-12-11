import RPi.GPIO as GPIO
import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info(event)

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Pins 20 and 21 will sense for button pushing
button1 = 20
button2 = 21

button_list = [button1, button2]

user1 = {'user': 'jeff'}
user2 = {'user': 'wualex'}
user_list = [user_1, user_2]

def lambda_handler(event, context):
    try:
        while True:
            # input_state = GPIO.input(button) # Sense the button
            pressed_btns = list(filter(lambda btn: GPIO.input(btn) == False), button_list)
            if len(pressed_btns) > 1:
                # just use the first pressed button
                button = pressed_btns[0]
                logger.info('Button ' + button + ' pressed')
                user = user_list[buttons.index(button)]
                logger.info('User ' + user + ' sent')
                myAWSIoTMQTTClient.publish(UPDATE_TOPIC, json.dumps(user), 0)
    finally:
        GPIO.cleanup()
