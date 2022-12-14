#!/usr/bin/env python3

#import tkinter
import datetime
import sys
import subprocess

class Uzivatel():

  def __init__(self, jmeno, vek, registrovan):
    self.jmeno = jmeno
    self.vek = vek
    self.registrovan = registrovan

  def __str__(self):
    return self.jmeno

class Databaze():

  uzivatele = []

  def __init__(self, soubor):
    self.soubor = soubor

  def pridejUzivatele(self, jmeno, vek, registrovan):
    u = Uzivatel(jmeno, vek, registrovan)
    self.uzivatele.append(u)

  def vratVsechny(self):
    seznam = []
    for uzivatel in self.uzivatele:
      seznam.append(uzivatel.jmeno)
    return seznam

  def nacti(self):
    self.uzivatele = []
    with open(self.soubor, "r", encoding="utf-8") as f:
      for s in f.readlines():
        jmeno, vek, registrovan = s.strip().split(";")
        registrovan = datetime.datetime.strptime(registrovan, "%d.%m.%Y")
        self.pridejUzivatele(jmeno, vek, registrovan)

  def uloz(self):
    with open(self.soubor, "w", encoding="utf-8") as f:
      for u in self.uzivatele:
        hodnoty = [u.jmeno, str(u.vek), u.registrovan.strftime("%d.%m.%Y")]
        radek = ";".join(hodnoty)
        f.write(radek + "\n")

class Aplikace():

  def __init__(self):
    self.report = "              Vitejte"
    self.vymazObrazovku()

  def vymazObrazovku(self):
    if sys.platform.startswith("win"):
      subprocess.call(["cmd.exe", "/C", "cls"])
    else:
      subprocess.call("clear")
    
  def vykresli(self):
    print("==================================")
    print(self.report)
    print("==================================")
    print("1 - nacti uzivatele z csv souboru")
    print("2 - vypis databazi")
    print("3 - pridej noveho uzivatele")
    print("4 - odstran uzivatele")
    print("5 - uloz databazi do csv souboru")
    print()
    print("0 - konec")
    vstup = str(input(">> "))
    return vstup
    
  def main(self, db):
    self.vymazObrazovku()
    report = self.vykresli()
    if report == "1":
      try:
        db.nacti()
        self.report = "Databaze je nactena"
      except:
        self.report = "Databazi se nepodarilo nacist."
    elif report == "2":
      self.report = db.vratVsechny()
    elif report == "3":
      pass
    elif report == "4":
      pass
    elif report == "5":
      db.uloz()
    else:
      sys.exit()

if __name__ == "__main__":
  d = Databaze("uzivatele.csv")
  a = Aplikace()
  while True:
    a.main(d)

