import machine
from machine import ADC
from machine import PWM
import utime

year = int(input("Year? "))
month = int(input("Month? "))
day = int(input("Day? "))
weekday = int(input("Weekday? "))  
hour = int(input("Hour? "))
minute = int(input("Minute? "))
second = int(input("Second? "))
microsecond = int(input("Microsecond? "))

rtc = machine.RTC()
rtc.datetime((year, month, day, weekday, hour, minute, second, microsecond))

# Timer callback function to display date and time
def display_datetime(timer):
    datetime = rtc.datetime() #retrieving current date and time
    formatted_date = f"{datetime[0]:04d}-{datetime[1]:02d}-{datetime[2]:02d})"
    formatted_time = f"{datetime[4]:02d}:{datetime[5]:02d}:{datetime[6]:02d}.{datetime[7]:06d}"
    print(f"Date: {formatted_date}\nTime: {formatted_time}\n")

# Setup hardware timer
timer = machine.Timer(0)
timer.init(period=30000, mode=machine.Timer.PERIODIC, callback=display_datetime)


pot = Pin(36, Pin.IN) # input signal from potentiometer

def ADC_potentiometer(tim):
    
    adc_pot = ADC(pot) # convert pot signal from analog to digital
    
# Setup hardware timer for pot signal
tim = machine.Timer(0)
tim.init(preriod=100, mode=machine.Timer.PERIODIC, callback=ADC_potentiometer)


led = Pin(13, Pin.OUT) # output LED

pwm = PWM(led, freq=10, duty_u16 = 512)





while True:
    pass



