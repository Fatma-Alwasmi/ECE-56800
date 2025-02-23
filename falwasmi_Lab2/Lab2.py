import machine
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


while True:
    pass



