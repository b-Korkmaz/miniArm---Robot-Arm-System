import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.IN)

pwm3 = GPIO.PWM(40,50)
pwm3.start(0)



pwm3.ChangeDutyCycle(5)
sleep(1)
pwm3.ChangeDutyCycle(0)
sleep(6)
pwm3.ChangeDutyCycle(2)
sleep(1)
pwm3.ChangeDutyCycle(0)

pwm3.stop()

#GPIO.setup(15, GPIO.IN)
#GPIO.setup(7, GPIO.IN)


while 1:
    
    sensor1= GPIO.input(11)
    sensor2 = GPIO.input(13)
    sensor3 = GPIO.input(15)
    sensor4 = GPIO.input(16)
    print("1.",sensor1)    
    print("2.",sensor2)
    print("3.",sensor3)
    print("4.",sensor4)
    sleep(3)
    """
    if(sensor1 ==1):
        
        print("1- Algılamadı")
        sleep(0.1)
    elif(sensor==0):
        print("1- Algıladı")
        sleep(0.1)
    elif(sensor2==1):
        print("2- Algılamadı")
        sleep(0.1)
    elif(sensor2==0):
        print("2- Algıladı")
        sleep(0.1)
    
     """


