#!/usr/bin/env python3

class Uzivatel:
  
  def __init__(self):
    celeJmeno = input("Jmeno a prijmeni:")
    self.next = True
    self.jmeno = ""
    self.prijmeni = ""
    try:  
      uzivatel = [celeJmeno.split(" ")[0], celeJmeno.split(" ")[1]]
      self.jmeno = uzivatel[0]
      self.prijmeni = uzivatel[1]
    except:
      self.next = False     

  def getName(self):
    return str(self.jmeno + " " + self.prijmeni)

uzivatele = []


while True:
  u = Uzivatel()
  if u.next == False:
    break
  else:
    uzivatele.append(u)
  

for i in range(len(uzivatele)):
  print(uzivatele[i].getName())

