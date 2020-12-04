#!/usr/bin/env python
"""
Maak een python script waarin je een Class definieert genaamd Liedje, die Class zal de tekst van een liedje laten zien.
De __init__() methode zou twee argumenten moeten hebben nl.: 'self' en 'tekst'. 'tekst' is een lijst. Maak binnen je
Class een method/function genaamd 'zingen' die elk element van de songtekst op zijn eigen regel afdrukt. Definieer een
variabele: 'verjaardagslied' die een object instantiëert van de Class.
"""


import time


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


class Liedje():
    def __init__(self, tekst):
        self.tekst = tekst

    def sing(self):
        for a in self.tekst:
            time.sleep(2.76190476)
            print(a)


liedje = Liedje(["Real hot girl shit", "Ah", "Body-ody-ody-ody-ody-ody-ody-ody","Ody-ody-ody-ody-ody-ody-ody (Mwah)",
                 "Body-ody-ody-ody-ody-ody-ody-ody", "Ody-ody-ody-ody-ody-ody-ody",
                 "Body crazy, curvy, wavy, big titties, lil' waist (Yeah, yeah, yeah)", "Body crazy, curvy, wavy, big "
                "titties, lil' waist (Mwah)", "Body-ody-ody-ody-ody-ody-ody-ody", "Ody-ody-ody-ody-ody-ody-ody",
                 "Look at how I bodied that, ate it up and gave it back (Ugh)", "Yeah, you look good, but they still "
                "wanna know where Megan at ", "(Where Megan at?)", "Saucy like a barbecue but you won't get your baby "
                "back", "See me in that dress and he feel like he almost tasted that (Ah, ah, ah)", "Num, num, num, num,"
                "eat it up, foreplay, okay, three, two, one", "You know I'm the hottest, you ain't ever gotta heat me "
                "up", "I'm present whеn I'm absent, speakin' when I'm not thеre", "All them bitches scary cats, I call "
                "'em Carole Baskins, ah", "Body-ody-ody-ody-ody-ody-ody-ody","Ody-ody-ody-"
                "ody-ody-ody-ody (Mwah)", "Body-ody-ody-ody-ody-ody-ody-ody", "Ody-ody-ody-ody-ody-ody-ody",
                 "Body crazy, curvy, wavy, big titties, lil' waist (Yeah, yeah, yeah)", "Body crazy, curvy, wavy, big "
                "titties, lil' waist (Mwah)", "Body-ody-ody-ody-ody-ody-ody-ody", "Ody-ody-ody-ody-ody-ody-ody",
                 "I'm a hot ebony, they gon' click it if it's me (If it's me)", "All my pictures been gettin' these "
                "niggas through the quarantine", "(Yeah)", "Bitch, I'm very well, on my shit as you could tell",
                 "Any ho got beef from years ago is beefing by herself, ah, ah", "If we took a trip on the real creep "
                "tip (Yeah)", "Bitch, rule number one is don't repeat that shit (Don't repeat that shit)",
                 "Rule number two, if they all came with you", "They better know exactly what the fuck they came to do "
                "(Yeah, yeah, yeah, woah, woah)", "Body-ody-ody-ody-ody-ody-ody-ody", "Ody-ody-ody-"
                "ody-ody-ody-ody (Mwah)", "Body-ody-ody-ody-ody-ody-ody-ody","Ody-ody-ody-ody-ody-ody-ody",
                 "Body crazy, curvy, wavy, big titties, lil' waist (Yeah, yeah, yeah)", "Body crazy, curvy, wavy, big "
                "titties, lil' waist (Mwah)","Body-ody-ody-ody-ody-ody-ody-ody", "Ody-ody-ody-ody-ody-ody-ody",
                 "The category is body, look at the way it's sittin' (Yeah)", "That ratio so out of control, that waist,"
                 "that ass, them titties (That waist, that ass, them titties)", "If I wasn't me and I would've seen "
                "myself, I would have bought me a drink (Hey)", "Took me home, did me long, ate it with the panties on "
                "(Ugh, ugh, ugh)", "I could build a house with all the brick I got (Yeah)", "Bitches spend a lifetime "
                "tryna get this hot (Tryna get this hot)", "And if her head too big, I could make that pop", "I'm not "
                "the one to play with like a touch-me-not, ah","Body-ody-ody-ody-ody-ody-ody-ody", "Ody-ody-ody-"
                "ody-ody-ody-ody (Mwah)", "Body-ody-ody-ody-ody-ody-ody-ody","Ody-ody-ody-ody-ody-ody-ody",
                 "Body crazy, curvy, wavy, big titties, lil' waist (Yeah, yeah, yeah)", "Body crazy, curvy, wavy, big "
                "titties, lil' waist (Mwah)","Body-ody-ody-ody-ody-ody-ody-ody", "Ody-ody-ody-ody-ody-ody-ody",
                 "Ody-ody-ody-ody", "Mwah"])

liedje.sing()
