#!/usr/bin/env python
"""
Info Print twee variabelen uit die optellen. De eerste variabele telt op elke seconde, de tweede elke twee seconden.
"""


import multiprocessing                          #to enable multiprocessing, to excecute multiple things at the same time
import time                                     #to use time


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Development"




def count_counter_1():                                 #to make counter 1
    COUNTER_1 = 0                                      #to start counter 1 at 0
    while True:
        COUNTER_1+=1                                   #to add 1 to the counter
        print('Counter 1:',COUNTER_1)                  #to print counter 1
        time.sleep(1)                                  #to wait 1 second

def count_counter_2():                                 #to make counter 1
    COUNTER_2 = 0                                      #to start counter 2 at 0
    while True:
        COUNTER_2+=1                                   #to add 1 to counter 2
        print('Counter 2:',COUNTER_2)                  #to print counter 2
        time.sleep(2)                                  #to wait 2 seconds


if __name__ == '__main__':                                          #code to execute if called from command-line
    PROCESS_ONE = multiprocessing.Process(target=count_counter_1)   #to create multiprocessing PROCESS_ONE
    PROCESS_TWO = multiprocessing.Process(target=count_counter_2)   #to create multiprocessing PROCESS_TWO
    PROCESS_ONE.start()                                             #to start multiprocessing PROCESS_ONE
    PROCESS_TWO.start()                                             #to start multiprocessing PROCESS_TWO