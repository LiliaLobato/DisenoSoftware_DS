from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum

##### Productos: son cascarones o esqueletos
class Estructura(ABC):
	def __init__(self, descripcion:str = None) -> None:
		self.__partes = []
		self.color = 'blanco'
		self.__descripcion = descripcion

	@property
	def partes(self) -> list:
		''' Retorna las aprtes del producto '''
		return self.__partes

	def agregar_parte(self, parte:str) -> None:
		''' Permite agregar un elemento a mi producto y controlar lo que se añada '''
		self.__partes.append(parte)

	def __str__(self) -> str:
		return self.__descripcion

# producto A1
class Auto(Estructura):
    def __init__(self):
        super().__init__('automovil')
# producto A2
class SUV(Estructura):
    def __init__(self):
        super().__init__('suv')
# producto A3
class Minivan(Estructura):
    def __init__(self):
        super().__init__('minivan')
# producto B1
class Motoneta(Estructura):
    def __init__(self):
        super().__init__('motoneta')
# producto B2
class MotoDeportiva(Estructura):
    def __init__(self):
        super().__init__('moto deportiva')
# producto B3
class Cuatrimoto(Estructura):
    def __init__(self):
        super().__init__('cuatrimoto')

##### Interfaz del Builder
class Honda(ABC):

	def __init__(self, tipo: tipoAuto) -> None:
		self.estructura = tipo.value

	def agregar_llantas(self, llantas:int = 2) -> None:
		''' Agrega llantas al producto '''
		self.estructura.agregar_parte(f'{llantas} llantas')
	def agregar_asientos(self, asientos:int = 1) -> None:
		''' Agrega asientos al producto '''
		print(type(self.estructura))
		self.estructura.agregar_parte(f'{asientos} asientos')
	def agregar_motor(self, motor:str = '10ltrs') -> None:
		''' Agrega motor al producto '''
		self.estructura.agregar_parte(f'Motor {motor}')
	def agregar_faros(self, faros:int = 1) -> None:
		''' Agrega faros al producto '''
		self.estructura.agregar_parte(f'{faros} faros')

	def contenido(self) -> list:
		return self.estructura.partes


##### Concrete Builder
class HondaAuto(Honda):
	''' Clase específica para crear auto '''
	class TipoAuto(Enum):
		AUTO 	= Auto()
		SUV 	= SUV()
		MINIVAN = Minivan()

	def __init__(self, tipo: tipoAuto) -> None:
		self.estructura = tipo.value

	def agregar_puertas(self, puertas:int = 2) -> None:
		''' Agrega puertas al producto '''
		self.estructura.agregar_parte(f'{puertas} puertas')
	def agregar_sistemaAudio(self, sistemaAudio:str = 'bocina') -> None:
		''' Agrega sistemaAudio al producto '''
		self.estructura.agregar_parte(f'Sistema de audio {sistemaAudio}')
	def agregar_quemacocos(self, quemacocos:int = 1) -> None:
		''' Agrega quemacocos al producto '''
		self.estructura.agregar_parte(f'{quemacocos} quemacocos')

class HondaMoto(Honda):
	''' Clase específica para crear auto '''
	class TipoAuto(Enum):
		MOTONETA 		= Motoneta()
		MOTODEPORTIVA 	= MotoDeportiva()
		CUATRIMOTO 		= Cuatrimoto()

	def __init__(self, tipo: tipoAuto) -> None:
		self.estructura = tipo.value

##### Director
class Fabrica:

	class Modelos(Enum):
		COMBI_ITESO = 'self.ensamblar_combi_iteso()'

	def __init__(self) -> None:
		self.__producto = None

	@property
	def producto(self) -> Honda:
		return self.__producto

	@producto.setter
	def producto(self, producto:Honda) -> None:
		self.__producto = producto

	def ensamblar_combi_ITESO(self) -> Honda:
		''' Ensambla combi para el iteso '''
		self.producto.agregar_asientos(4)
		self.producto.agregar_faros(2)
		self.producto.agregar_llantas(8)
		self.producto.agregar_motor('5.1 litros turbo cargado')
		self.producto.agregar_puertas(5)
		self.producto.agregar_quemacocos()
		self.producto.agregar_sistemaAudio('Harman Kardon')
		return self.producto.contenido()

	def iniciar_montaje(self, tipo:Modelos):
		''' Inicia montaje '''
		eval(tipo.value)


# Cliente
if __name__ == '__main__':
	fabrica = Fabrica()
	fabrica.producto = HondaAuto(HondaAuto.TipoAuto.MINIVAN)
	print(fabrica.ensamblar_combi_ITESO())