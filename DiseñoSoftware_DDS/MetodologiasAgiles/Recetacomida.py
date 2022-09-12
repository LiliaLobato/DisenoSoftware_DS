# 24/Ago/2022
from abc import ABC, abstractmethod
# Libreria Recetas de Comida

# Interface: define la estructura y comportamiento por defecto
#            intermediario entre el codigo del cliento y mi codigo
class RecetaComida(ABC):

	def __init__ (self, nombre:str, tiempo:int, descripcion:str, ingredientes:str) -> None:
		self.nombre = nombre
		self.tiempo = tiempo
		self.descripcion = descripcion
		self.ingredientes = ingredientes

	def MiReceta(self) -> str:
		''' Retorna la informacion detallada de la receta en str '''
		return f'La receta {self.nombre} va a tomar {self.tiempo} min.\nNecesitamos los ingredientes: {self.ingredientes}\nMetodo de preparacion:\n{self.descripcion}'

	@abstractmethod
	def ResumenReceta(self) -> str:
		''' Retorna el tipo de comida y nombre de la receta en str '''
		pass

# Clase concreta
class CocinaItaliana(RecetaComida):

	def MiReceta(self) -> str:
		''' Retorna la informacion de la receta italiana en str '''
		return f'\n--- COMIDA ITALIANA ---\n{super().MiReceta()}'
	
	def ResumenReceta(self) -> str:
		''' Retorna el tipo de comida como italiana y nombre de la receta en str '''
		return f'Comida Italiana - {self.nombre}'

# Clase concreta
class CocinaMexicana(RecetaComida):

	def MiReceta(self) -> str:
		''' Retorna la informacion de la receta mexicana en str '''
		return f'\n--- COMIDA MEXICANA ---\n{super().MiReceta()}'

	def ResumenReceta(self) -> str:
		''' Retorna el tipo de comida como mexicana y nombre de la receta en str '''
		return f'Comida Mexicana - {self.nombre}'

# Clase concreta
class CocinaJaponesa(RecetaComida):

	def MiReceta(self) -> str:
		''' Retorna la informacion de la receta japonesa en str '''
		return f'\n--- COMIDA JAPONESA ---\n{super().MiReceta()}'

	def ResumenReceta(self) -> str:
		''' Retorna tipo de comida como japonesa y nombre de la receta en str '''
		return f'Comida Japonesa - {self.nombre}'

if __name__ == '__main__':
	# Declaramos una receta y bebidas
	ramen = CocinaJaponesa('Ramen', 30, 'Es una sopa', 'huevo, agua, noodles')
	
	# Imprimimos la informacion detallada de las recetas
	print(ramen.MiReceta())

	# Imprimimos la informacion simplificada de las recetas de comida
	print(ramen.ResumenReceta())
	
	

