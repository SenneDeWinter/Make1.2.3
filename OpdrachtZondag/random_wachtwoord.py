#!/usr/bin/env python
"""
Een python script dat random wachtwoorden genereert.

    zowel kleine letters als grote, cijfers en tekens
    op aanvraag de complexiteit (aantal tekens en soort tekens)
    maak gebruik van flowcontrol en functies!
"""


import random


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


tekens = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?./:+=~><_-&@#1234567890'


def main():
    global tekens
    aantal = input("Hoeveel wachtwoorden wil je genereren?  ")
    aantal = int(aantal)
    lengte = input("Hoe lang moet je wachtwoord zijn?  ")
    lengte = int(lengte)
    for a in range(aantal):
        wachtwoord = ''
        for b in range(lengte):
            wachtwoord += random.choice(tekens)
            print(f"Dit is je nieuwe wachtwoord  {wachtwoord}")


if __name__ == '__main__':    #code to execute if called from command-line
    main()