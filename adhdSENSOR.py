import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

trig = 23
echo = 24

print "measuring distance"

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

gpio.output(trig, False)

print "stopcalmdown"
time.sleep(2)

gpio.output(trig, True)
time.sleep(0.00001)
gpio.output(trig, False)

print "sent signal"

while gpio.input(echo)==0:
    print gpio.input(echo)
    pulse_start=time.time()

print "recived signal"

while gpio.input(echo)==1:
    print gpio.input(echo)
    pulse_end=time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150
distane = round(distance, 2)
print "Distance: ",distance,"cm"
gpio.cleanup()
