import RPi.GPIO as GPIO

import time
import os


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(25,GPIO.OUT)



red_led = GPIO.PWM(25,100)

red_led.start(0)

pause_time = 0.1



print("1st Stage")
for x in range (100):
                        red_led.ChangeDutyCycle(30)

                        time.sleep(pause_time)


print("2nd Stage")
for x in range (100):
                        red_led.ChangeDutyCycle(50)

                        time.sleep(pause_time)

print("3rd Stage")
for x in range (100):
                        red_led.ChangeDutyCycle(70)

                        time.sleep(pause_time)

print("final Stage")
for x in range (100):
                        red_led.ChangeDutyCycle(100)

                        time.sleep(pause_time)


GPIO.cleanup()

print("Done")


