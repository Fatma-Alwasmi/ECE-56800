import network
import ntptime
import machine
from machine import RTC, Timer
import time

# connect to WI-FI network


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

rtc = RTC()


def get_date_time():
    
    ntptime.settime() # connect to NTP server pool.ntp.org
    current_time = time.localtime(time.time() ) # get UTC time and conver to EST time - 4 * 3600
    
    # set tral-timer clock to current time fetched above
    rtc.datetime((current_time[0], current_time[1], current_time[2],   # year, month, day
                  current_time[3],                                    # weekday
                  current_time[4], current_time[5], current_time[6], current_time[7])) # hour, minute, second, microsec
    
def display_date_time(timer):
    now = rtc.datetime() # retrieves current date/time that was prev set by get_date_time()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    print(f" Date: {now[1]:02d}/{now[2]:02d}/{now[0]:04d} {weekdays[now[3]]}")  # mm/dd/yyyy weekday 
    print(f"Time: {now[4]:02d}:{now[5]:02d}:{now[6]:02d}:{now[7]:06d} HRS") # hr:min:sec:microsec HRS
    
do_connect()   
get_date_time()
timer = Timer(0)
timer.init(period = 15000, mode=Timer.PERIODIC, callback=display_date_time)

