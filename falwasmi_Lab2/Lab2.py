from machine import RTC, Timer, ADC, PWM, Pin
import utime

# get user input for date and time
year = int(input("Year? "))
month = int(input("Month? "))
day = int(input("Day? "))
weekday = int(input("Weekday? "))  
hour = int(input("Hour? "))
minute = int(input("Minute? "))
second = int(input("Second? "))
microsecond = int(input("Microsecond? "))

# initialize RTC
rtc = RTC()
rtc.datetime((year, month, day, weekday, hour, minute, second, microsecond))

# timer callback function to display date and time
def display_datetime(timer):
    datetime = rtc.datetime()  
    formatted_date = f"{datetime[0]:04d}-{datetime[1]:02d}-{datetime[2]:02d}"
    formatted_time = f"{datetime[4]:02d}:{datetime[5]:02d}:{datetime[6]:02d}.{datetime[7]:06d}"
    print(f"Date: {formatted_date}\nTime: {formatted_time}\n")

# setup hardware timer for RTC display
datetime_timer = Timer(0)
datetime_timer.init(period=30000, mode=Timer.PERIODIC, callback=display_datetime)

# setup ADC for potentiometer
pot = Pin(36, Pin.IN)
adc_pot = ADC(pot)
adc_pot.atten(ADC.ATTN_11DB)  # attenuation for full range 0-3.3V

# timer callback function to read input pot
def adc_potentiometer(timer):
    pot_value = adc_pot.read()  


# setup hardware timer for pot readings
pot_timer = Timer(1)
pot_timer.init(period=100, mode=Timer.PERIODIC, callback=adc_potentiometer)

# setup PWM for LED
led = Pin(13, Pin.OUT)
pwm_led = PWM(led, freq=10, duty_u16=512)  

while True:
    pass  

