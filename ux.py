#!/usr/bin/env python3


class Uzivatel():
  
  def __init__(self, jmeno, vek, registrovan):
    self.jmeno = jmeno
    self.vek = vek
    self.registrovan = registrovan

  def __str__(self):
    return self.jmeno

import lxml.etree as ET
import datetime

uzivatele_list = []

uzivatele_list.append(Uzivatel("Adam Novak",22,datetime.datetime(2022,5,6)))
uzivatele_list.append(Uzivatel("Jan Novak",20,datetime.datetime(2021,7,8)))
uzivatele_list.append(Uzivatel("Martin Novak",28,datetime.datetime(2020,10,5)))

uzivatele = ET.Element("uzivatele")

for u in uzivatele_list:
  uzivatel = ET.SubElement(uzivatele, "uzivatel")
  uzivatel.set("vek", str(u.vek))
  jmeno = ET.SubElement(uzivatel, "jmeno")
  jmeno.text = u.jmeno
  reg = ET.SubElement(uzivatel, "registrovan")
<<<<<<< HEAD
  reg.text = str(u.registrovan.strftime("%d.%mmmm.%Y")) 
=======
  reg.text = str(u.registrovan.strftime("%d.%m.%Y")) 
>>>>>>> cc0360fe24b52b12e6c8ccc6d8c5c1eab21e0012

soubor = ET.tostring(uzivatele, pretty_print=True, xml_declaration=True, encoding="utf-8")
f = open("uzivatele.xml", "wb")
f.write(soubor)
f.close()


<<<<<<< HEAD
=======













>>>>>>> cc0360fe24b52b12e6c8ccc6d8c5c1eab21e0012
