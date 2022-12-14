#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Kostka:
	"""
	Trida reprezentujici hraci kostku.
	"""

	def __init__(self, pocetSten=6):
		self.__pocetSten = pocetSten

	def getPocetSten(self):
		"""
		Vrati pocet sten kostky.
		"""
		return self.__pocetSten
	
	def hod(self):
		"""
		Vykona hod kostkou a vrati cislo od 1 do poctu sten.
		"""
		import random as _random
		return _random.randint(1, self.__pocetSten)

	def __str__(self):
		"""
		Vraci textovou reprezentaci kostky.
		"""
		return str("Kostka s {0} stenami.".format(self.__pocetSten))

class Bojovnik:
	"""
	Trida reprezentujici bojovnika do areny.
	"""

	def __init__(self, jmeno, zivot, utok, obrana, kostka):
		"""
		jmeno - jmeno bojovnika
		zivot - maximalni zivot bojovnika
		utok - utok bojovnika
		obrana - obrana bojovnika
		kostka - instance kostky
		"""

		self._jmeno = jmeno
		self._zivot = zivot
		self._maxZivot = zivot
		self._utok = utok
		self._obrana = obrana
		self._kostka = kostka
		self._zprava = ""
	
	def __str__(self):
		return str(self._jmeno)

	@property
	def nazivu(self):
		return self._zivot > 0
	
	def grafickyUkazatel(self, aktualni, maximalni):
		celkem = 20
		pocet = int(aktualni / maximalni * celkem)
		if pocet == 0 and self.nazivu:
			pocet = 1
		return "[{0}{1}]".format("#"*pocet," "*(celkem-pocet))
	
	def grafickyZivot(self):
		return self.grafickyUkazatel(self._zivot, self._maxZivot)

	def branSe(self, utok):
		zraneni = utok - (self._obrana + self._kostka.hod())
		if zraneni > 0:
			zprava = "{0} utrpel zraneni o sile {1}.".format(self._jmeno, zraneni)
			self._zivot = self._zivot - zraneni
			if self._zivot < 0:
				self._zivot = 0
				zprava = zprava[:-1] + " a zemrel."
		else:
			zprava = "{0} zcela odrazil utok.".format(self._jmeno)
		self._setZprava(zprava)
	
	def utoc(self, souper):
		uder = self._utok + self._kostka.hod()
		zprava = "{0} utoci uderem o sile {1}.".format(self._jmeno, uder)
		self._setZprava(zprava)
		souper.branSe(uder)
	
	def _setZprava(self, zprava):
		self._zprava = zprava

	def getZprava(self):
		return self._zprava

class Arena:
	
	def __init__(self, bojovnik1, bojovnik2, kostka):
		self.__bojovnik1 = bojovnik1
		self.__bojovnik2 = bojovnik2
		self._kostka = kostka
	
	def __vykresli(self):
		self.__vycistiObrazovku()
		print("-------------- Arena s bojovniky --------------\n")
		print("Bojovnici:")
		self.__vypisBojovnika(self.__bojovnik1)
		self.__vypisBojovnika(self.__bojovnik2)
	
	def __vycistiObrazovku(self):
		import sys as _sys
		import subprocess as _subprocess
		if _sys.platform.startswith("win"):
			_subprocess.call(["cmd.exe", "/C", "cls"])
		else:
			_subprocess.call("clear")
	
	def __vypisZpravu(self, zprava):
		import time as _time
		print(zprava)
		_time.sleep(0.8)
	
	def __vypisBojovnika(self, bojovnik):
		print(bojovnik)
		print("Zivot: {0}".format(bojovnik.grafickyZivot()))
		if isinstance(bojovnik, Mag):
			print("Mana: {0}".format(bojovnik.grafickaMana()))
	
	def zapas(self):
		import random as _random

		print("Vitejte v Arene!")
		print("Dnes se utkaji {0} a {1}".format(self.__bojovnik1, self.__bojovnik2))
		print("Zapas muze zacit...", end=" ")
		input()

		if(_random.randint(0,1)):
			(self.__bojovnik1, self.__bojovnik2) = (self.__bojovnik2, self.__bojovnik1)
		while(self.__bojovnik1.nazivu and self.__bojovnik2.nazivu):
			self.__bojovnik1.utoc(self.__bojovnik2)
			self.__vykresli()
			self.__vypisZpravu(self.__bojovnik1.getZprava())
			self.__vypisZpravu(self.__bojovnik2.getZprava())
			if(self.__bojovnik2.nazivu):
				self.__bojovnik2.utoc(self.__bojovnik1)
				self.__vykresli()
				self.__vypisZpravu(self.__bojovnik2.getZprava())
				self.__vypisZpravu(self.__bojovnik1.getZprava())

			print("")

class Mag(Bojovnik):
	
	def __init__(self, jmeno, zivot, utok, obrana, kostka, mana, magickyUtok):
		super().__init__(jmeno, zivot, utok, obrana, kostka)
		self.__mana = mana
		self.__maxMana = mana
		self.__magickyUtok = magickyUtok
	
	def utoc(self, souper):
		if self.__mana < self.__maxMana:
			self.__mana = self.__mana + 10
			if self.__mana > self.__maxMana:
				self.__mana = self.__maxMana
			super().utoc(souper)
		else:
			uder = self.__magickyUtok + self._kostka.hod()
			zprava = "{0} pouzil magii za {1} hp.".format(self._jmeno, uder)
			self._setZprava(zprava)
			self.__mana = 0
			souper.branSe(uder)
	
	def grafickaMana(self):
		return self.grafickyUkazatel(self.__mana, self.__maxMana)
	


