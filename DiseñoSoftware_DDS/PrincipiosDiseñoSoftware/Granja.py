# 28/Ago/2022
from __future__ import annotations
import random

#Clase A
class Granja:
	''' Representa al principal objeto que agrega elementos de la clase B '''
	def __init__(self, nombre:str, granjero:str, hectareas:int=5, animales:list=[], numero_cultivos:int=2) -> None:
		self.nombre:str = nombre
		self.granjero:str = granjero
		# Restringimos el acceso haciendolo privado
		self.__hectareas:int = hectareas
		# Relacion de AGREGACION
		self.animales:list = animales
		# Relacion de COMPOSICION
		self.cultivos = []
		for _ in range(numero_cultivos):
			self.cultivos.append(Cultivo())

	def __str__(self) -> str:
		''' Retorna los datos de la granja '''
		return f'---GRANJA "{self.nombre}", {self.hectareas} hectareas\nEl granjero {self.granjero} tiene {len(self.animales)} animales y {len(self.cultivos)} tipos de cultivo'

	def __del__(self) -> str:
		''' Retorna informacion de la granja que se elimina '''
		#print(f'La granja {self.nombre} cerró')
		return(f'La granja {self.nombre} cerró')

	def vender(self, otro:Granja, cantidad_hectareas:int) -> str:
		''' Simula la venta de N hectareas de una granja a otra '''
		self.hectareas -= cantidad_hectareas
		otro.hectareas += cantidad_hectareas
		return (f'Venta de {cantidad_hectareas} hectareas de {self.nombre} a {otro.nombre}')

	def mostrar_cultivos(self) -> str:
		''' Retorna todos los tipos de cultivo que tiene la granja '''
		ret_cultivos = f'El granjero {self.granjero} cultiva: '
		sep = ''
		for cultivo in self.cultivos:
			ret_cultivos = ret_cultivos + sep + cultivo.planta
			sep = ', '
		return ret_cultivos

	# GETTER
	@property
	def hectareas(self) -> int:
		''' Propiedad que retorna el valos del atributo hectareas '''
		return self.__hectareas

	# SETTER
	@hectareas.setter
	def hectareas(self, valor:int) -> None:
		''' Propiedad que asigna el valos del atributo hectareas '''
		if valor < 0:
			raise Exception('No se permiten valores negativos para esta propiedad')
		self.__hectareas = valor

#Clase B 
class Animales:
	''' Contiene el objeto el cual sera agregado a la clase A ''' 
	def __init__(self, especie:str, cantidad:int=1, precio_unitario:int=300) -> None:
		self.especie:str = especie
		self.cantidad:int = cantidad
		self.precio_unitario:int = precio_unitario

	def __str__(self) -> str:
		''' Retorna la informacion del Animales '''
		return f'{self.especie}:\n{self.cantidad} unidades, ${self.precio_unitario} c/u'

#Clase C
class Cultivo:
	''' Contiene el objeto el cual sera asocioados a la clase A ''' 
	def __init__ (self) -> None:
		self.planta = random.choice(['zanahoria','manzana', 'naranjas', 'jitomates', 'papas'])

	def __str__(self) -> str:
		''' Retorna la infroamcion del cultivo '''
		return f'Cultivando {self.planta}'

	def __del__(self) -> None:
		''' Retorna informacion del cultivo que se elimina '''
		#print(f'Se terminó la temporada de {self.planta}')
		return (f'Se terminó la temporada de {self.planta}')

if __name__ == '__main__':
	# Componentes
	print('\n--- Creamos los animales (Componentes Agregados) ---')
	conejos = Animales('Conejo', 20, 300)
	patos = Animales('Pato', 5, 500)
	vacas = Animales('Vaca', 10, 5000)
	pollos = Animales('Pollo', 50, 400)
	print(conejos)
	print(patos)
	print(vacas)
	print(pollos)

	# Contenedores
	print('\n--- Creamos los animales (Contenedores) ---')
	granja_milagros = Granja('El Milagro','Don Juan', 15, [conejos, patos, pollos], 3)
	granja_vaca_feliz = Granja('La Vaca Feliz','Don Pepe', 40,  [vacas], 7)
	print(granja_milagros)
	print('')
	print(granja_vaca_feliz)

	print('\n--- Imprimimos los cultivos (Componentes Asociados) ---')
	print(granja_milagros.mostrar_cultivos())
	print(granja_vaca_feliz.mostrar_cultivos())

	print('\n--- Vendemos tierra ---')
	print(granja_vaca_feliz.vender(granja_milagros, 20))
	
