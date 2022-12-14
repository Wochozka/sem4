#!/usr/bin/env python3

# Tento soubor je prakticky stejný, jen lze zadat vstupní a výstupní soubor jako parametr spuštění
# Příklad 1: ./prevod2_parametry.py -i uzivatele.csv
# Příklad 2: ./prevod2_parametry.py -i uzivatele.csv -o uzivatele.xml

import lxml.etree as ET
import argparse             # modul pro rozpoznávání parametrů
import sys                  # potřebné pro ověřování verze (balík systémových modulů)

class Uzivatel:
    """
    Tato třída bude plodit objekty načtené ze souboru .csv
    """

    def __init__(self, jmeno, vek, registrovan):
        self._jmeno = jmeno
        self._vek = vek
        self._registrovan = registrovan      # na objekt datetime kašleme (odstraněn i z importů)

    def __str__(self):                       # textová reprezentace je tu navíc, nikde se neprojevuje
        return str(self._jmeno)

class Prevod:
    def __init__(self, vstup, vystup=None):  # instance třídy Prevod očekává zadání vstupního souboru, výstupní soubor
        if vstup == None:
            print("Chybí vstupní CSV soubor pro převod. \n Type prevod2_parametry.py -h for help.")
            sys.exit(-1)
        if vystup == None:                   # můžeme vynechat; pokud tak učiníme, bude 'None' a vygeneruje se ze vstupu
            vystup = vstup[:-4] + ".xml"
        self._vstup = vstup
        self._vystup = vystup
        self._zaznamy = []                   # zde vytvoříme seznam, kde budou objekty třídy Uzivatel

    def nacti(self):                         # metoda s minimálními změnami oproti té z hodiny (prevod.py)
        with open(self._vstup, "r", encoding="utf-8") as f:
            for s in f.readlines():
                jmeno, vek, registrovan = s.strip().split(";")
                u = Uzivatel(jmeno, vek, registrovan)
                self._zaznamy.append(u)

    def uloz(self):                             # metoda zůstala prakticky beze změn, jen názvy proměnných se vrátily
        uzivatele = ET.Element("uzivatele")

        for u in self._zaznamy:
            uzivatel = ET.SubElement(uzivatele, "uzivatel")
            uzivatel.set("vek", u._vek)
            jmeno = ET.SubElement(uzivatel, "jmeno")
            jmeno.text = str(u._jmeno)
            reg = ET.SubElement(uzivatel, "registrovan")
            reg.text = str(u._registrovan)
        xml = ET.tostring(uzivatele, pretty_print=True, xml_declaration=True, encoding="utf-8")
        f = open(self._vystup, "wb")
        f.write(xml)
        f.close()

def cmdline_args():
    """
    Metoda pro zpracování argumentů (parametrů) z příkazové řádky
    """
    # Vytvoření objektu pro parsování (zpracování) parametrů
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-i", "--input", help="define input .csv file path")  # do parametru 'help'je mořné napsat jakoukoli nápovědu
    p.add_argument("-o", "--output", help="define output .xml file path")

    return p.parse_args()


if __name__=="__main__":                        # pokud spouštíme program z konzole (vestavná podmínka)
    # nejprve je nutné ověřit verzi nainstalovaného Pythonu, jinak nebude modul argparse dostupný a bude
    # třeba jej doinstalovat příkazem pip install argparse
    if sys.version_info<(3,5,0):
        sys.stderr.write("You need python 3.5 or later to run this script\n")
        sys.exit(1)
    try:
        args = cmdline_args()                   # zavoláme metodu pro zpracování argumentů a její výstup uložíme do 'args'
    except:
        print('See "prevod2_parametry.py -h" for help.')

    p = Prevod(args.input, args.output)
    p.nacti()                                   # metody nacti() a uloz() by mohly být spojené do jedné, např. preved()
    p.uloz()                                    # zde jsou odděleny jen pro názornost
