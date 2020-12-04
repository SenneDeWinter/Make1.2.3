#!/usr/bin/env python
"""
Een python script dat random wachtwoorden genereert.

    zowel kleine letters als grote, cijfers en tekens
    op aanvraag de complexiteit (aantal tekens en soort tekens)
    maak gebruik van flowcontrol en functies!
"""


import random                                                                          #to generate random passwords


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


tekens = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?./:+=~><_-&@#1234567890' #to set the possible characters


def main():
    global tekens
    aantal = input("Hoeveel wachtwoorden wil je genereren?  ")                     #to ask for the amount of passwords
    aantal = int(aantal)                                                           #to initialize the amount of password
    lengte = input("Hoe lang moet je wachtwoord zijn?  ")                          #to ask how long the password must be
    lengte = int(lengte)                                                           #to initialize the length
    for a in range(aantal):
        wachtwoord = ''                                                            #to initialize an empty password
        for b in range(lengte):
            wachtwoord += random.choice(tekens)                                    #to generate a password
            print(f"Dit is je nieuwe wachtwoord  {wachtwoord}")                    #to print the password


if __name__ == '__main__':    #code to execute if called from command-line
    main()