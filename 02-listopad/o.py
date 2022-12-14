#!/usr/bin/env python3

class Uzivatel:
  
  def __init__(self, jmeno, prijmeni):
    self.jmeno = jmeno
    self.prijmeni = prijmeni

def addNewUser():
  jmeno = input("Jmeno:")
  prijmeni = input("Prijmeni:")
  uzivatel = Uzivatel(jmeno, prijmeni)
  return uzivatel

uzivatele = []
for a in range(5):
  uzivatele.append(addNewUser())  

for a in range(len(uzivatele)):
  print(uzivatele[a].jmeno, uzivatele[a].prijmeni)

