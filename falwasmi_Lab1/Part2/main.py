import machine
from machine import Pin
import time
from neopixel import NeoPixel

count = 0
button = Pin(38,Pin.IN)
NEOPIXEL_PIN = 0
NEOPIXEL_POWER_PIN = 2
power_pin = Pin(NEOPIXEL_POWER_PIN, Pin.OUT)
power_pin.value(1)
led = NeoPixel(machine.Pin(NEOPIXEL_PIN), 1)
while True:
    led[0] = (255,0,0)
    led.write()
    if button.value() == 0:
        led[0] = (0,255,0)
        led.write()
        time.sleep(0.3)
        print(count)
        count += 1
    if count == 5:
        print("You have successfully implemented LAB1")
        power_pin.value(0)
        break
    


