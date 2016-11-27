import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.IN)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

ledDic = {1:18,2:23,3:24,4:25,5:12,6:16,7:20}

def led (led, on):
	if on:
		GPIO.output(ledDic[led],GPIO.HIGH)
	else:
		GPIO.output(ledDic[led],GPIO.LOW)

def blinkLed (ledNo):
	led(ledNo,True)
	time.sleep(.1)
	led(ledNo,False)

def ride ():
	blinkLed(1)
	blinkLed(2)
	blinkLed(3)
	blinkLed(4)
	blinkLed(5)
	blinkLed(6)
	blinkLed(7)
	blinkLed(6)
	blinkLed(5)
	blinkLed(4)
	blinkLed(3)
	blinkLed(2)

os.system('clear')
print "NightRider"

mode = "0"
mode = input("Which mode do you want to run? 1: auto 2: button? (1/2)")

if mode == 1:
	loopCount = 0
	loopCount = input("How many times should NightRider to loop?: ")
	print "Will run", loopCount, "times"
	while loopCount > 0:
		print "Runs left: ", loopCount
		loopCount = loopCount - 1
		ride ()
elif mode == 2:
	print "Press and hold the button to Nightrider"
	while True:	
		while GPIO.input(17) == False: #button pressed	
			ride ()
		while GPIO.input(17) == True: #button release
			for key in ledDic:
				led(key,False)		
			time.sleep(1)
			for key in ledDic:
				led(key,True)						
			time.sleep(1)
else:
	print "Invalid selection"
