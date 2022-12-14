#!/usr/bin/env python3

PWD = "/home/ucitel/Svarc/2022-23/Sem4"

def vycisti():
  import sys
  import subprocess
  if sys.platform.startswith("win"):
    subprocess.call(["cmd.exe", "/C", "cls"])
  else:
    subprocess.call("clear")


def ulozit(nazev, text, mode="a"):

  with open(nazev, mode, encoding="utf-8") as f:
    f.write(text)
  

def nacist(nazev):

  with open(nazev, "r") as f:
    for radek in f.readlines():
      print(radek.strip())

def menu():
  print("1 - Nacteni souboru")
  print("2 - Zapsani do souboru")
  print("3 - Prepsani souboru")
  print("4 - Konec")
  print("5 - Vycisti obrazovku")
  print("")

while True:
  menu()
  c = int(input(">> "))
  if c == 1:
    vycisti()
    print()
    nacist("pokus.txt")
    print()
  elif c == 2:
    content = input("Zadej obsah: ")
    print(content + "\n")
    ulozit("pokus.txt", content + "\n")
  elif c == 3:
    content = input("Zadej obsah: ")
    ulozit("pokus.txt", content, mode="w")
  elif c == 4:
    exit()
  elif c == 5:
    vycisti()
  else:
    pass
  


