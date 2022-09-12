# 5/SEP/2022

from __future__ import annotations
from enum import Enum, unique

class Producto:
	def __init__ (self, descripcion:list, cantidad:list, precio:float) -> None:
		self.descripcion = descripcion
		self.cantidad = cantidad
		self.precio = precio

class Orden:

	''' Encapsulamiento a nivel de clase en donde nosotros podemos definir mas	paises en un futuro '''
	@unique
	class Pais(Enum):
		# name = value
		MEXICO 	= 0.20
		USA 	= 0.07
		COSTA_RICA = 0.12

	def __init__ (self, pais:Pais) -> None:
		self.pais:Orden.Pais = pais
		self.productos:list = []

	def agregar (self, producto: Producto) -> None:
		''' Agrega productos al carrito de comparas '''
		self.productos.append(producto)

	def total_orden(self) -> float:
		''' Retorna el valor total de la orden al leer cada producto y aplicar impuestos '''
		total = 0
		for p in self.productos:
			total += p.precio * p.cantidad
		total += total*self.pais.value

		return total 


#Codigo cliente
if __name__ == '__main__':
	carrito = Orden(Orden.Pais.COSTA_RICA)
	carrito.agregar(Producto('Blusas azules', 4, 1200))
	carrito.agregar(Producto('Reloj', 1, 5800))
	carrito.agregar(Producto('Blusas amarillas', 6, 800))

	print(carrito.total_orden())