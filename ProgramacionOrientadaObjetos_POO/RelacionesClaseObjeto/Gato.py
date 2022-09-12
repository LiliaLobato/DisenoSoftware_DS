# 5/SEP/2022

from __future__ import annotations
from enum import Enum, unique
from abc import ABC

class Comida(ABC):
	''' Reglas y politicas de la iterfase comida ''' 
	@property
	def energia(self) -> int:
		''' Retorna la energia del raton '''
		return self._energia

class Gato:
	def __init__ (self) -> None:
		self.__energia = 100

	def alimentar(self, comida:Productos) -> str:
		''' Retorna el nivel de energia despues de alimentar al gato '''
		self.__energia += comida.energia
		return self.__energia

	@property
	def energia(self) -> int:
		''' Retorna la energia del gatito '''
		return self.__energia


class Salchicha(Comida):
	def __init__(self) -> None:
		self._energia = 30


class Raton(Comida):
	def __init__(self) -> None:
		self._energia = 85

class Productos(Enum):
	SALCHICHA 	= Salchicha()
	RATON 		= Raton()


#Codigo cliente
if __name__ == '__main__':
	tom = Gato()
	print(f'Antes de comer: {tom.energia}')
	tom.alimentar(Raton())
	print(f'Despues de comer: {tom.energia}')