#!/usr/bin/env python
"""
Maak een functie die data (bv. van een sensor) in een lijst stopt. Er worden steeds 20 items in de lijst gestoken,
het gemiddelde print je af. Zorg dat je de loop kan onderbreken met een door jou gekozen symbool/letter/nummer/...
"""


import random


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Development"


def print_list(j=False):
    while True:
        lijst = []
        for i in range(20):
            lijst.append(random.randint(1, 900))
            i += 1
        print(lijst)
        gemiddelde = sum(lijst)/len(lijst)
        print(gemiddelde)
        if input("Wil je Stoppen? j/n:  ") == j:
            break


if __name__ == '__main__':    #code to execute if called from command-line
    print_list()