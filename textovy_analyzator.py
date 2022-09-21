"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomas Benko
email: tomas.benko.tb@gmail.com
discord: Tomas B.#3206
"""

import pandas as pd
import numpy as np
import os
import pprint

uzivatele = {"bob":"123","ann":"pass123","mike":"password123","liz":"pass123"}

uzivatele["user"] = ("bob","ann","mike","liz")
uzivatele["password"] = ("123","pass123","password123","pass123")
print(uzivatele["user"])

jmeno = input("Prihlasovaci jmeno: ")
heslo = input("Heslo: ")

if uzivatele.get(jmeno) == heslo:
    print(f"""Dobry den, {jmeno}, prosim, nyni muzes zacit analyzovat texty.""")
else:
    print("ciao")