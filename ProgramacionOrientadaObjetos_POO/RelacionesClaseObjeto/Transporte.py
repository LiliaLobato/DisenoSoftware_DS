# 5/SEP/2022
# LOBATO MARTINEZ, LILIA ARCELI
# ARIAS IBARRA, SERGIO ALEJANDRO
# FIGUEROA MONTAÑO, CHRISTIAN ERNESTO


from __future__ import annotations
from enum import Enum, unique
from abc import ABC

# Interface
class Motor(ABC):
    def mover(self) -> str:
        ''' Retorna el tipo de maquina '''
        return f'Moviendonos con una {self._tipo} ...'
    
    @property
    def tipo(self) -> str:
    	''' Retorna la maquina '''
    	return self._tipo

# Clases concretas
class MotorCombustion(Motor):
    def __init__(self, tipo:str='máquina de combustión') -> None:
        self._tipo = tipo

class MotorElectrico(Motor):
    def __init__(self, tipo:str='máquina electrica') -> None:
        self._tipo = tipo


# Interface
class Chofer(ABC):
    def manejar(self) -> str:
        ''' Retorna el piloto tipo de piloto '''
        return f'Un {self._piloto} está manejando...'

    @property
    def piloto(self) -> str:
    	''' Retorna el piloto '''
    	return self._piloto

# Clases concretas
class Robot(Chofer):
    def __init__(self, piloto:str='robot') -> None:
        self._piloto = piloto

class Humano(Chofer):
    def __init__(self, piloto:str='humano') -> None:
        self._piloto = piloto

# Clase Transporte
class Transporte:
	def __init__ (self, motor:TipoMotor, chofer:Chofer, destino:str = '', carga:int = 0) -> None:
		self.motor = motor.value
		self.chofer = chofer
		self.__destino = destino
		self.__carga = carga

	def entregar (self, destino:str, carga:int) -> str:
		''' Retorna el destino y el tamaño de la carga '''
		self.__destino = destino
		self.__carga = carga
		return f'Transporte con destino a {self.__destino}, con una carga de {self.__carga}kg'

	def __str__(self) -> str:
		''' Retorna el tipo de maquina y quien la maneja '''
		return f'Una {self.motor.tipo} manejado por {self.chofer.piloto}'

	''' Encapsulamiento a nivel de clase en donde nosotros podemos definir mas motores en un futuro '''
	@unique
	class TipoMotor(Enum):
		# name = value
		COMBUSTION 	= MotorCombustion()
		ELECTRICO 	= MotorElectrico()

if __name__ == '__main__':
    # Creamos el tipo de chofer que manejará el transporte
    chofer = Humano()

    # Creamos el objeto transporte
    tesla = Transporte(Transporte.TipoMotor.ELECTRICO, chofer)
    print(tesla)
    print(tesla.entregar('GDL', 10))

    print(tesla.chofer.manejar())
    print(tesla.motor.mover())
