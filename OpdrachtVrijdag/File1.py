#!/usr/bin/env python
"""
Je programmeert je huisinstallatie:
    -Je werkt met een Raspberry Pi en programmeert je code in Python.
    -Je leest de toestand van de drukknop in.
    -Wanneer er op de drukknop wordt gedrukt zal de juiste reeks lampen branden (functionaliteit kies je zelf.
     2 drukknoppen dus minstens 2 lampen).
    -Je lampen zijn verbonden met een relais.
    -De drukknoppen sturen de lampen aan met multiprocessing
"""


from gpiozero import LED                        #to use LED from gpiozero
from gpiozero import Button                     #to use Button from gpiozero
import multiprocessing                          #to use multiprocessing
from gpiozero.pins.pigpio import PiGPIOFactory  #to use the remote GPIO pins
import time                                     #to use time in the code


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Development"


IP = PiGPIOFactory(host='192.168.1.39') #to set the Raspberry Pi IP adress to '....', to use the GPIO pins on this IP

LED_1= LED(16, pin_factory=IP)          #to set LED_1 to remote GPIO pin 16
LED_2= LED(20, pin_factory=IP)          #to set LED_2 to remote GPIO pin 20

BUTTON_1= Button(26,pin_factory=IP)     #to set BUTTON_1 to remote GPIO pin 26
BUTTON_2 = Button(19, pin_factory=IP)   #to set BUTTON_2 to remote GPIO pin 19


def set_leds_on_off():                    #to turn the leds turn on or off
    while True:                           #to repeat this function untill program is stopped
        if BUTTON_1.is_pressed:           #to do something if BUTTON_1 is pressed
            time.sleep(0.5)               #to wait half a second, to debounce the button
            LED_1.toggle()
            LED_2.toggle()


def set_leds_on_30seconds():                        #to turn the leds on for 30 seconds
    while True:                                     #to repeat this function untill program is stopped
        if BUTTON_2.is_pressed:                     #to do something if BUTTON_2 is pressed
            LED_1.on()
            LED_2.on()
            time.sleep(30)                          #to wait 30 seconds
            LED_1.off()
            LED_2.off()


if __name__ == '__main__':                                               #code to execute if called from command-line
    PROCESS_ONE = multiprocessing.Process(target=set_leds_on_off)        #to create multiprocessing PROCESS_ONE
    PROCESS_TWO = multiprocessing.Process(target=set_leds_on_30seconds)  #to create multiprocessing PROCESS_TWO
    PROCESS_ONE.start()                                                  #to start multiprocessesing PROCESS_ONE
    PROCESS_TWO.start()