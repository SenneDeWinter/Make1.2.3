#!/usr/bin/env python
"""
Programmeer 3 drukknoppen. Elke drukknop stuurt een LED aan. De LED blijft 5 seconden aan en gaat dan uit.
"""


import time                                     #to use time
from gpiozero import Button                     #to use a button
from gpiozero import LED                        #to use a LED
from gpiozero.pins.pigpio import PiGPIOFactory  #to use the remote RPI GPIO pins
import multiprocessing                          #to use multiprocessing, to execute multiple things at once


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Development"


IP=PiGPIOFactory(host='192.168.1.39')      #to set the remote GPIO adress to 192.168.1.39

LED_1=LED(16,pin_factory=IP)               #to set the LED to a GPIO pin
LED_2=LED(20,pin_factory=IP)
LED_3=LED(21,pin_factory=IP)


BUTTON_1=Button(26, pin_factory=IP)        #to set the button to a GPIO pin
BUTTON_2=Button(19, pin_factory=IP)
BUTTON_3=Button(13, pin_factory=IP)

def set_led_1():
    while True:
        if BUTTON_1.is_pressed:           #to do something if the button is pressed
            LED_1.on()
            time.sleep(5)                 #to wait for 5 seconds
            LED_1.off()

def set_led_2():
    while True:
        if BUTTON_2.is_pressed:           #to do something if the button is pressed
            LED_2.on()
            time.sleep(5)                 #to wait for 5 seconds
            LED_2.off()

def set_led_3():
    while True:
        if BUTTON_3.is_pressed:          #to do something if the button is pressed
            LED_3.on()
            time.sleep(5)                #to wait for 5 seconds
            LED_3.off()

if __name__ == '__main__':                                     #code to execute if called from command-line
    PROCESS_ONE = multiprocessing.Process(target=set_led_1)    #to create multiprocessing PROCESS_ONE
    PROCESS_TWO = multiprocessing.Process(target=set_led_2)    #to create multiprocessing PROCESS_TWO
    PROCESS_THREE = multiprocessing.Process(target=set_led_3)  #to create multiprocessing PROCESS_THREE
    PROCESS_ONE.start()                                        #to start multiprocessing PROCESS_ONE
    PROCESS_TWO.start()                                        #to start multiprocessing PROCESS_TWO
    PROCESS_THREE.start()                                      #to start multiprocessing PROCESS_THREE