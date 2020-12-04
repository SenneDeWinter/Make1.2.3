#!/usr/bin/env python
"""
Maak een functie die data (bv. van een sensor) in een lijst stopt. Er worden steeds 20 items in de lijst gestoken,
het gemiddelde print je af. Zorg dat je de loop kan onderbreken met een door jou gekozen symbool/letter/nummer/...
"""


import random                                           #to use random numbers


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Development"


def print_list(j=False):
    while True:                                        #to do something until it's stopped
        lijst = []                                     #to create an empty list
        for i in range(20):                            #to do something 20 times
            lijst.append(random.randint(1, 900))       #to add 20 numbers to a list
            i += 1
        print(lijst)                                   #to print the list
        gemiddelde = sum(lijst)/len(lijst)             #to calculate the average
        print(gemiddelde)                              #to print the average
        if input("Wil je Stoppen? j/n:  ") == j:       #to ask if the user wants to stop
            break                                      #to end the loop


if __name__ == '__main__':    #code to execute if called from command-line
    print_list()