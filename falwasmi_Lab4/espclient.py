import network
import ntptime
import machine
import esp32  
from machine import RTC, Timer, Pin
from neopixel import NeoPixel
import time
import socket


#---------2.2 Connect to the Interned over Wi-Fi-----------
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
    
do_connect()


#---------2.3.2 ESP32 Program-----------

def measure_send(time):
    temp = esp32.raw_temperature()
    hall = esp32.hall_sensor()
    print(f"Onboard temperature sensor data: {temp}F, Hall sensor data: {hall}")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockaddr = socket.getaddrinfo('api.thingspeak.com', 80)[0][-1]
        s.connect(sockaddr)
        s.send(f"GET https://api.thingspeak.com/update?api_key=BJWYVA81B229O2CQ&field1={temp}&field2={hall} HTTP/1.0\r\n\r\n")
        s.recv(1024)
    except:
        pass
    finally:
        s.close()
        


timer1 = Timer(0);
timer1.init(period = 30000, mode=Timer.PERIODIC, callback=measure_send)






