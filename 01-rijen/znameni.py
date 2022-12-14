#!/usr/bin/env python3
# -*- coding: utf-8 -*-

znameni = ['střelec', 'kozoroh','vodnář','ryba',
	'beran','býk','blíženec','rak',
	'lev','panna','váhy','štír','hadonoš']

data = [20,46,71,108,133,171,200,220,256,300,323,329,347]

datNar = input("Zadej datum narozeni ve formatu DD.MM.RRRR:")
datNar = datNar.split(".")
denNar = int(datNar[0])
mesNar = int(datNar[1])
denVRoce = ((30*mesNar)-30)+denNar

i = 1
for a in data:
	if(denVRoce > a):
		vysledek = znameni[i]
	elif(denVRoce < data[0]):
		vysledek = znameni[0]
		break
	i = i + 1
	if(i > 12):
		i=0

print("Jsi znamením", vysledek + ".")


