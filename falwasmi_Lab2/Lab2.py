from machine import RTC, Timer, ADC, PWM, Pin

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
    formatted_date = f"{datetime[1]:02d}/{datetime[2]:02d}/{datetime[0]:04d}"
    formatted_time = f"{datetime[4]:02d}:{datetime[5]:02d}:{datetime[6]:02d}:{datetime[7]:06d}"
    print(f"Date: {formatted_date}\nTime: {formatted_time}\n")

# setup hardware timer for RTC display
datetime_timer = Timer(0)
datetime_timer.init(period=30000, mode=Timer.PERIODIC, callback=display_datetime)


# setup ADC for potentiometer
pot = Pin(36, Pin.IN)
adc_pot = ADC(pot)
adc_pot.atten(ADC.ATTN_11DB)  # attenuation for full range 0-3.3V
pressed = 0
# setup PWM signal for LED
led = Pin(13, Pin.OUT)
pwm_led = PWM(led, freq=10, duty_u16=512)  

# timer callback function to read input pot
def control_led(timer):
    global pressed
    pot_val = adc_pot.read()
    
    if pressed == 1:
        new_freq = max(1, (pot_val * 100) // 4095)
        pwm_led.freq(new_freq)
        pwm_led.duty_u16(512)
        

    elif pressed == 2:
        new_duty = (pot_val * 65535) // 4095
        pwm_led.duty_u16(new_duty)
        pwm_led.freq(100)
        
        
    else:
        pwm_led.freq(10)
        pwm_led.duty_u16(512)
        
        


# setup hardware timer for pot readings
pot_timer = Timer(1)
pot_timer.init(period=100, mode=Timer.PERIODIC, callback=control_led)


def detect_switch(pin):
    global pressed
    
    if switch.value() == 1:

        if pressed == 0:
            pressed = 1
            
        elif pressed == 1:
            pressed = 2
                  
        elif pressed == 2:
            pressed = 1
            
    
debounce_timer = Timer(2)
switch = Pin(38, Pin.IN, Pin.PULL_DOWN)

def debounce_switch(pin):
    debounce_timer.init(mode=Timer.ONE_SHOT, period=200, callback=detect_switch)


switch.irq(handler=debounce_switch, trigger=Pin.IRQ_FALLING)
    
while True:
    
    pass

