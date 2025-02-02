import machine
from machine import Pin
import time
from neopixel import NeoPixel

count = 0
button = Pin(38,Pin.IN)
power_pin = Pin(2, Pin.OUT)
power_pin.value(1)
led = NeoPixel(machine.Pin(0), 1)
while count != 5:
    led[0] = (255,0,0) #led ->red
    led.write()
    while button.value() == 0: # pressed
        led[0] = (0,255,0) #led ->green
        led.write()
        print(count)
        if button.value() == 1: #unpressed
            count += 1

print("You have successfully implemented LAB1")
power_pin.value(0)
