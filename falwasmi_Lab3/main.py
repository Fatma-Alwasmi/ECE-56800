import network
import ntptime
import machine
import esp32  
from machine import RTC, Timer, Pin
from neopixel import NeoPixel
import time

# -----------2.2.4.1. Wake up Sources-----------
led_gpio = Pin(13, Pin.OUT)  
led_gpio.value(1)  # Turn red LED ON when awake

# Check wake-up reason at startup
if machine.wake_reason() == machine.PIN_WAKE:
    print("Woke up due to EXT0 wakeup")
else:
    print("Woke up due to Timer wake up")

# -----------2.2.1.Connect to the Internet over WiFi-----------
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting to network...")
        wlan.connect('hotbreakfast', 'boxcutter')
        while not wlan.isconnected():
            pass
        ssid = wlan.config("essid")
        IP = wlan.ifconfig()[0]
        print(f"Connected to {ssid}")
        print(f"IP Adress: {IP}")

def get_date_time():
    ntptime.settime() # connect to NTP server pool.ntp.org
    current_time = time.localtime(time.time() - 4 * 3600) # get UTC time and convert to EST time 
    # set real-timer clock to current time fetched above  
    rtc.datetime((current_time[0], current_time[1], current_time[2],     # year, month, day
                  current_time[6],                                       # weekday
                  current_time[3], current_time[4], current_time[5], 0)) # hr, min, sec, microsec 

# -----------2.2.2. Display Current Date and Time using Network Time Protocol (NTP)-----------
def display_date_time(timer):
    now = rtc.datetime() # retrieves current date/time that was prev set by get_date_time()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(f"Date: {now[1]:02d}/{now[2]:02d}/{now[0]:04d} {weekdays[now[3]]}")  # mm/dd/yyyy weekday 
    print(f"Time: {now[4]:02d}:{now[5]:02d}:{now[6]:02d} HRS") # hr:min:sec:microsec HRS

rtc = RTC()
do_connect()
get_date_time()
timer1 = Timer(0)
timer1.init(period = 15000, mode=Timer.PERIODIC, callback=display_date_time)

# -----------2.2.3. NeoPixel Control by Touch Input-----------
touch = machine.TouchPad(Pin(12, machine.Pin.IN))
power_pin = Pin(2, Pin.OUT)
power_pin.value(1)
led_neopixel = NeoPixel(machine.Pin(0), 1)

def detect_touch(timer):
    # not touched
    if touch.read() >= 100:
        led_neopixel[0] = (0, 0, 0)
        led_neopixel.write()
    else:
        led_neopixel[0] = (0, 255, 0)
        led_neopixel.write()
        
timer2 = Timer(1)
timer2.init(period = 50, mode=Timer.PERIODIC, callback=detect_touch)

# -----------2.2.4. Red LED, Deep Sleep, and Different Wake Up Sources-----------
def go_to_sleep(timer):
    print("I am going to sleep for 1 minute.")
    
    wake_pin = Pin(14, Pin.IN, Pin.PULL_UP)
    esp32.wake_on_ext0(pin=wake_pin, level=esp32.WAKEUP_ALL_LOW)
    
    led_gpio.value(0)
    machine.deepsleep(60000)
    
timer3 = Timer(2)
timer3.init(period=30000, mode=Timer.PERIODIC, callback=go_to_sleep)
