import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

#FL 36, 32, 11
#FR 40, 38, 7
#BL 35, 27, 13
#BR 33, 31, 15

ma = #
mb = #
pwm = #

GPIO.setup(ma, GPIO.OUT)
GPIO.setup(mb, GPIO.OUT)
GPIO.setup(pwm, GPIO.OUT)

GPIO.output(ma, GPIO.LOW)
GPIO.output(mb, GPIO.LOW)

p = GPIO.PWM(pwm, 1000)
p.start("Running")

while 1:
    GPIO.output(ma, GPIO.HIGH)
    GPIO.output(mb, GPIO.LOW)
    print("Forward")
GPIO.cleanup()





