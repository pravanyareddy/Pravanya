import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
x=0
while(x<=1):
          GPIO.output(35, 1)
	  print "ON 1"
	  time.sleep(0.5)
	  GPIO.output(35, 0)
	  print "OFF 1"
	  time.sleep(0.5)
	  GPIO.output(38, 0)
	  print "ON 2"
	  time.sleep(0.5)
	  GPIO.output(38, 1)
	  print "OFF 2"
	  time.sleep(0.5)
	  x=x+1
