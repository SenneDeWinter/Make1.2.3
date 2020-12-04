#!/usr/bin/env python
"""
Maak een functie die data (bv. van een sensor) in een lijst stopt. Er worden steeds 20 items in de lijst gestoken,
het gemiddelde print je af. Zorg dat je de loop kan onderbreken met een door jou gekozen symbool/letter/nummer/...
"""


import random
import time
from pynput import keyboard
import multiprocessing


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Development"


def end_program():
    break_program = False

def on_press(key):
    global break_program
    if key == keyboard.Key.end:
        break_program = True
        return False
    with keyboard.Listener(on_press=on_press) as listener:
        while break_program == False:
            time.sleep(5)
        listener.join()


def print_list():
    while True:
        lijst = []
        i = 0
        for i in range(20):
            lijst.append(random.randint(1, 33))
            i += 1
        time.sleep(2)
        print(lijst)
        gemiddelde = sum(lijst)/len(lijst)
        print(gemiddelde)


if __name__ == '__main__':    #code to execute if called from command-line
    PROCESS_ONE = multiprocessing.Process(target=print_list)
    PROCESS_TWO = multiprocessing.Process(target=end_program)
    PROCESS_THREE = multiprocessing.Process(target=on_press)
    PROCESS_ONE.start()
    PROCESS_TWO.start()
    PROCESS_THREE.start()