# 24/Ago/2022
import Recetacomida as recetas

class Recetario:

	def __init__ (self, nombre:str, autor:str, prefacio:str, recetas:list) -> None:
		self.nombre = nombre
		self.autor = autor
		self.prefacio = prefacio
		self.recetas = recetas

	def Indice(self, RecetaComida) -> bool:
		''' Retorna un resumen de la receta si esta es de comida '''
		if (isinstance(RecetaComida, recetas.RecetaComida)):
			return RecetaComida.ResumenReceta()

	# Magic Method / Dunder Method
	def __str__(self) -> str:
		''' Retorna el objeto como str '''
		return f'\"{self.nombre}\", {self.autor}\n{self.prefacio}'


# Declaramos las recetas
ramen = recetas.CocinaJaponesa('Ramen', 30, 'Es una sopa', 'huevo, agua, noodles')
tacos = recetas.CocinaMexicana('Tacos', 10, 'Es un taco', 'carne, tortilla, salsa')
spaguetti = recetas.CocinaItaliana('Spaguetti', 40, 'Es un ramen seco', 'spaguetti, salsa, carne, jitomate')

# Declaramos nuestro recetario
LibroRecetario = Recetario('Recetas buenas, bonitas y baratas', 
							'Lilia Lobato', 
							'Compendio de recetas faciles de preparar, ricas y economicas',
							[ramen, tacos, spaguetti])
print(LibroRecetario)

# Imprimimos el indice
print('--- INDICE ---')
for platillo in LibroRecetario.recetas:
	print(LibroRecetario.Indice(platillo))

# Imprimimos los detalles de una receta
print(ramen.MiReceta())