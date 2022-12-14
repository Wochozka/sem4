#!/usr/bin/env python3

vstup = ".csv"
vystup = vstup[:-4] + ".xml"
def nacti():
    uzivatele = []
    with open(vstup, "r", encoding="utf-8") as f:
        for s in f.readlines():
            jmeno, vek, registrovan = s.strip().split(";")
            registrovan = datetime.datetime.strptime(registrovan, "%d.%m.%Y")
            self.pridejUzivatele(jmeno, vek, registrovan)
