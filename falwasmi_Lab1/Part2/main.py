from machine import Pin
from time import sleep

led_board = Pin(0, Pin.OUT)

# Toggle LED 5 times

for i in range(10):
    led_board.value(not led_board.value())
    sleep(0.5)

print("LED blinked 5 times")

    

