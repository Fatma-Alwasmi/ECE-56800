ESP32 V2 Laboratory Projects – ECE 56800 (Spring 2025)

This repository bundles the four lab assignments completed for Purdue University’s ECE 56800 – Embedded  Systems course.All firmware is written in MicroPython 1.20+ and targets the Espressif ESP32‑V2 DevKit (dual‑core, 2 MB PSRAM).Each lab focuses on a different subsystem or programming concept; together they form a small but realistic IoT showcase.

Hardware Bill‑of‑Materials

Module / Part

Minimum Qty

Used in Lab

Notes

ESP32‑V2 DevKit

1

all

On‑board red LED → GPIO 13

NeoPixel (single RGB LED)

1

1 (Part 2), 3

Data pin → GPIO 0

Tactile push‑button

1

1 (Part 2), 2, 3

Pull‑down on GPIO 38 / GPIO 14

10 kΩ Potentiometer

1

2

Wiper → GPIO 37 (ADC 1 ch0), ends to 3V3 & GND

Misc. wires, breadboard

–

all



Wi‑Fi with Internet

–

3, 4

SSID: hotbreakfast / Pass: boxcutter (change in code!)

Lab Reference

Lab 1 – Getting Started

Part

File(s)

Purpose

1

program1.py – program5.py

Short exercises: string formatting, list filtering, Fibonacci generator, guessing game, two‑sum index finder. Run them with desktop Python 3 to confirm interpreter basics.

2

main.py

Blink on‑board LED (GPIO 13) ten times with 500 ms period.

 

switchpress.py

Count five button presses (GPIO 38) while showing NeoPixel red→green state changes. Demonstrates polling vs. busy wait and simple state machines.

Lab 2 – Real‑Time Clock & Analog I/O

Lab2.py

Features

User enters date/time at boot → RTC initialized (machine.RTC).

Hardware timer 0 prints current timestamp every 30 s.

Potentiometer on ADC channel controls:

Mode 1 (pressed once): LED PWM frequency (1 Hz–100 Hz).

Mode 2 (pressed twice): LED PWM duty (0–100 %).Switch debounced with a one‑shot timer on GPIO 38.

Lab 3 – Networking, Touch, and Power Management

main.py

Joins Wi‑Fi network and syncs RTC via NTP (ntptime).

Periodic timer prints local date/time (EST).

Capacitive touch pad on GPIO 14 drives a NeoPixel status LED.

After 30 s of activity the board enters deep‑sleep for 60 s; it can also be woken by a low level on the same touch pin. Wake reason is reported over serial.

Lab 4 – Cloud Telemetry and Local Web Control

Script

Role

espclient.py

Headless client that measures on‑chip temperature & Hall sensor, then pushes them to ThingSpeak (HTTP GET) every 30 s.

espserver.py

Minimal HTTP server: returns a responsive HTML dashboard with live sensor readings and two buttons to switch the red LED ON/OFF.


