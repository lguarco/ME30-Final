import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

#FL 36, 32, 11
#FR 40, 38, 7
#BL 35, 27, 13
#BR 33, 31, 15

ma1 = 36
mb1 = 32
pwm1 = 11

ma2 = 40
mb2 = 38
pwm2 = 7

ma3 = 35
mb3 = 27
pwm3 = 13

ma4 = 33
mb4 = 31
pwm4 = 15

#Motor 1
GPIO.setup(ma1, GPIO.OUT)
GPIO.setup(mb1, GPIO.OUT)
GPIO.setup(pwm1, GPIO.OUT)

GPIO.output(ma1, GPIO.LOW)
GPIO.output(mb1, GPIO.LOW)

#Motor 2
GPIO.setup(ma2, GPIO.OUT)
GPIO.setup(mb2, GPIO.OUT)
GPIO.setup(pwm2, GPIO.OUT)

GPIO.output(ma2, GPIO.LOW)
GPIO.output(mb2, GPIO.LOW)

#Motor 3
GPIO.setup(ma3, GPIO.OUT)
GPIO.setup(mb3, GPIO.OUT)
GPIO.setup(pwm3, GPIO.OUT)

GPIO.output(ma3, GPIO.LOW)
GPIO.output(mb3, GPIO.LOW)

#Motor 4
GPIO.setup(ma4, GPIO.OUT)
GPIO.setup(mb4, GPIO.OUT)
GPIO.setup(pwm4, GPIO.OUT)

GPIO.output(ma4, GPIO.LOW)
GPIO.output(mb4, GPIO.LOW)

#PWM Set up!
a = GPIO.PWM(pwm1, 1000)
b = GPIO.PWM(pwm2, 1000)
c = GPIO.PWM(pwm3, 1000)
d = GPIO.PWM(pwm4, 1000)

a.start(50)
b.start(50)
c.start(50)
d.start(50)


while 1:
    GPIO.output(ma1, GPIO.HIGH)
    GPIO.output(mb1, GPIO.LOW)

    GPIO.output(ma2, GPIO.HIGH)
    GPIO.output(mb2, GPIO.LOW)

    GPIO.output(ma3, GPIO.HIGH)
    GPIO.output(mb3, GPIO.LOW)

    GPIO.output(ma4, GPIO.HIGH)
    GPIO.output(mb4, GPIO.LOW)
    print("Forward")

GPIO.cleanup()





