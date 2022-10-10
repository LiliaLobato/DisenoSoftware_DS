# ---------------------------------------------------------------------------------------------
# * Equipo: N
# Nombre de los integrantes del equipo
# - Lilia Arceli Lobato Martinez
# ---------------------------------------------------------------------------------------------

from __future__ import annotations
from abc import ABC
from time import sleep
from enum import Enum, unique

class Personaje:

    SALUD_PERSONAJE = 100

    def __init__(self, nombre:str):
        self.nombre = nombre
        self.mochila = None
        self.vida = self.SALUD_PERSONAJE
    
    def comer(self, alimento:Alimentos) -> None:
        ''' El personaje consume los alimentos para ganar vida '''
        carne = self.mochila.getAlimento(alimento,True)
        if carne != None:
            self.vida += carne.aporte_vida
            self.mochila.eliminarCarne(alimento, carne)
            print(f'Comí {carne}, +{carne.aporte_vida} vida')

class Mochila:

    # ---------------------------------------------------------------------------------------------
    # * RETO
    # ---------------------------------------------------------------------------------------------
    # Objetivo: Reemplazar los números con variables de clase.

    ESPACIADORES = 50
    DESGASTE = 10
    DESGASTEMINIMO = 1

    '''
    La mochila tiene la capacidad de guardar un número limitado de artículos
    '''
    def __init__(self, nombre:str, max_items:int=5):
        self.nombre = nombre
        self._max_items = max_items
        self.items = {}

    # ---------------------------------------------------------------------------------------------
    # * RETO
    # ---------------------------------------------------------------------------------------------
    # Objetivo: Consolidad las expresiones en las condicionales
    
    @unique
    class Objetos(Enum):
        # name = value
        RAMITA      = 'ramita'
        ROCA        = 'roca'
        CUERDA      = 'cuerda'
        PEDERNAL    = 'pedernal'
        PEPITA_ORO  = 'pepita oro'
        CESPED      = 'cesped'
        TRONCO      = 'tronco'

        def __str__(self) -> str:
            return self.value

    # ---------------------------------------------------------------------------------------------
    # * RETO
    # ---------------------------------------------------------------------------------------------
    # Existe código que se repite constantemente
    # Objetivo: Evitar duplicidad de código en cada una de las ramas de las condicionales

    def espacioEnMochila(self) -> bool:
        ''' Retorna si hay espacio en la maleta '''
        return len(self.items) < self._max_items

    def guardadoPreviamente(self, trinket:Enum) -> bool:
        ''' Retorna si el trinket está guardado en la maleta '''
        return trinket in self.items

    def isHerramienta(self, trinket:Enum) -> bool:
        ''' Retorna si es una herramienta el trinket '''
        return isinstance(trinket, Herramientas)

    def isAlimento(self, trinket:Enum) -> bool:
        ''' Retorna si es una herramienta el trinket '''
        return isinstance(trinket, Alimentos)

    def getAlimento(self,alimento, isCocido=False):
        if self.guardadoPreviamente(alimento):
            for carne in self.items[alimento]:
                if carne.cocido == isCocido:
                    return carne
        return None

    def getHerramienta(self,herramienta):
        return self.items[herramienta][0]

    # ---------------------------------------------------------------------------------------------
    # * RETO
    # ---------------------------------------------------------------------------------------------
    # Objetivo: recoger colecciones de objetos a la mochila. Los objetos se pueden agrupar. No hace
    # falta conocer el numero de objetos. Actualmente solo es posible incluir los nombres de los
    # articulos.
        
    def recoger(self, trinket:Enum, cantidad:int = 1) -> bool:
        ''' Ingresa articulos en la mochila '''
        if self.espacioEnMochila():
            if self.isHerramienta(trinket): 
                return self.recogerHerramienta(trinket)            
            if self.isAlimento(trinket): 
                return self.recogerAlimento(trinket)
            else:
                return self.recogerObjeto(trinket, cantidad)
          
        else:
            print(f'Se alcanzo la capacidad máxima de tu mochila, {self._max_items} en total')
            return False
            #raise ValueError(f'Se alcanzo la capacidad máxima de tu mochila, {self._max_items} en total')

    def recogerHerramienta(self, herramienta:Enum) -> bool:
        ''' Añada una herramienta a la mochila, retorna True si se pudo añadir'''
        herramientaCls = Herramientas.getHerramienta(self, herramienta.value)

        if self.existeVersionHerramienta(herramientaCls):
            print(f'Se tiene una versión diferente del objeto {str(herramienta.value)} en tu mochila')
            return False
            #raise ValueError(f'Se tiene una versión diferente del objeto {str(herramienta)} en tu mochila')

        if self.guardadoPreviamente(herramienta):
            self.items[herramienta].append(herramientaCls)
        else: 
            self.items[herramienta] = [herramientaCls]

        print(f'Se añadió: {str(herramientaCls)}')
        return True

    def recogerAlimento(self, alimento:Enum) -> bool:
        ''' Añada un alimento a la mochila, retorna True si se pudo añadir '''
        alimentoCls = Alimentos.getAlimento(self, alimento.value)

        if self.guardadoPreviamente(alimento):
            self.items[alimento].append(alimentoCls)
        else: 
            self.items[alimento] = [alimentoCls]

        print(f'Se añadió: {str(alimentoCls)}')
        return True

    def recogerObjeto(self, objeto:Enum, cantidad:int) -> bool:
        ''' Añade un objeto a la maleta,  retorna True si se pudo añadir '''
        if self.guardadoPreviamente(objeto):
            self.items[objeto] += cantidad
        else:
            self.items[objeto] = cantidad

        print(f'Se añadió: {cantidad} {str(objeto)}')
        return True

    # ---------------------------------------------------------------------------------------------
    # * RETO
    # ---------------------------------------------------------------------------------------------
    # Objetivo: Poder guardar herramientas dentro de la mochila, pero una version de la herramienta
    # a la vez. Por ejemplo, no se puede tener un Hacha normal y un Hacha de lujo en la misma mochila.
    
    def existeVersionHerramienta(self, herramienta:Herramientas) -> bool:
        ''' Revisa si existe una versión diferente a la herramienta en la mochila '''
        if(isinstance(herramienta, Hacha)):
            for key in self.items.keys():
                herramientaCls = Herramientas.getHerramienta(self, key.value)
                if isinstance(herramientaCls, Hacha):
                    return herramientaCls.version != herramienta.version
        else:
            return False

    # ---------------------------------------------------------------------------------------------
    # * RETO
    # ---------------------------------------------------------------------------------------------
    # La lógica de las condicionales parece algo compleja 
    # Objetivo: Crear métodos para el manejo de las expresiones en las condicionales

    def fabricar(self, herramienta:Herramientas) -> bool:
        '''
        Fabricar herramientas a través de los artículos en tu inventario. Regresa True si se pudo
        fabricar la herramienta
        '''
        herramientaCls = Herramientas.getHerramienta(self, herramienta.value)
        if self.recetaHerramientaCompleta(herramientaCls) and self.recoger(herramienta):            
            self.quitarObjetosReceta(herramientaCls)
            return True
        else:
            return False

    def recetaHerramientaCompleta(self, herramienta:object) -> bool:
        ''' retorna True si la mochila contiene suficientes objetos para construir una herramienta '''
        for key, value in herramienta.receta.items():
            if not self.suficientesMateriales(key, value): 
                print(f'No hay suficientes materiales para una {str(herramienta)}, falta {str(key)}')
                return False
        return True
    
    def suficientesMateriales(self, objeto:object, cantidad = 1 ) -> bool:
        ''' revisa si la maleta contiene suficientes objetos '''
        if self.guardadoPreviamente(objeto):
            return self.items[objeto] >= cantidad
        return False

    def quitarObjetosReceta(self, herramienta:object) -> None:
        ''' Elimina un objeto de la mochila o reduce la cantidad guardada '''
        for key, value in herramienta.receta.items():
            self.items[key] -= value
            if self.items[key] == 0 : 
                self.items.pop(key)
    
    def contenidoMochila (self, trinket:Enum) -> str:
        ''' Retorna un string con los objetos y herramientas de la mochila '''
        if self.isHerramienta(trinket[0]):
            return str(trinket[0].value) + ': ' + str(len(trinket[1]))
        if self.isAlimento(trinket[0]):
            return str(trinket[0].value) + ': ' + ',  '.join(map(str, trinket[1]))
        return str(trinket[0]) + ': ' + str(trinket[1])

    def __str__(self) -> str:
        ''' Retorna un string con los trinkets de la mochila '''
        list_items = '\n'.join(map(self.contenidoMochila, self.items.items()))
        return f'''\n{self.nombre:^{self.ESPACIADORES}}\n{"="*self.ESPACIADORES}\n{list_items}\n'''

    # ---------------------------------------------------------------------------------------------
    # * RETO
    # ---------------------------------------------------------------------------------------------
    # Objetivo: Agrega el metodo "demoler" con un "assert" el cual suponga que se tiene al menos
    # 1 de durabilidad antes de ejecutar la acción.

    def demoler(self, herramienta:Enum):
        ''' Retorna True cuando una herramienta demuele, la herramienta sufre un desgaste '''
        if not self.isHerramienta(herramienta) or herramienta == Herramientas.FOGATA:
            print(f'No puedes demoler con {herramienta.value}')
            return False 

        if self.guardadoPreviamente(herramienta):
            herramientaActual = self.getHerramienta(herramienta)
            assert herramientaActual.durabilidad > self.DESGASTEMINIMO, f'El {herramienta} está inservible'

            herramientaActual.durabilidad -= self.DESGASTE
            if herramientaActual.durabilidad > self.DESGASTEMINIMO:
                print(f'Se usó el {herramienta.value}, durabilidad = {herramientaActual.durabilidad}')
            else:
                self.eliminarHerramienta(herramienta)
                print(f'Se usó el {herramienta.value} y se rompió')            
            return True
        else:
            print(f'No tienes {herramienta.value} en tu mochila')
            return False

    def eliminarHerramienta(self, herramienta:Enum) -> None:
        self.items[herramienta].pop(0)
        if len(self.items[herramienta]) == 0:
            self.items.pop(herramienta)

    def cocinar(self, alimento:Alimentos) -> bool:
        ''' Retorna True cuando un alimento se puede cocinar, el alimento se guarda en la maleta '''
        if self.guardadoPreviamente(Herramientas.FOGATA.value):
            print(f'No tienes una {Herramientas.FOGATA} en tu mochila')
            return False
        carne = self.getAlimento(alimento)
        if carne == None:
            print(f'No tienes {alimento.value} crudo en tu mochila')
            return False
        else:
            print(f'Se cocinó {alimento.value}')
            self.getHerramienta(Herramientas.FOGATA).cocinar(carne)
            return True

    def eliminarCarne(self, alimento:Enum, carne) -> None:
        self.items[alimento].remove(carne)
        if len(self.items[alimento]) == 0:
            self.items.pop(alimento)

class Martillo:
    '''
    El martillo es una herramienta que se puede utilizar para demoler estructuras.
    El martillo requiere 3 rocas, 3 ramitas y 2 cuerdas para que se pueda fabricar.
    La durabilidad es el número de usos.
    '''
    def __init__(self, durabilidad:int=15, daño:int=17):
        self.durabilidad = durabilidad
        self.daño = daño
        #TODO: receta puede ser un diccionario! es mas facil de leer y de manejar
        self.receta = {Mochila.Objetos.ROCA: 3, Mochila.Objetos.RAMITA: 3, Mochila.Objetos.CUERDA: 3}
        self.version = 'Martillo'

    def __str__(self) -> str:
        ''' Retorna la versión de la herramienta '''
        return str(self.version)


class Hacha:
    '''
    El hacha es una herramienta que se puede utilizar para talar árboles. Se puede crear
    al comienzo del juego con 1 ramita y 1 pedernal.
    '''
    def __init__(self, durabilidad:int=100, daño:int=27):
        self.durabilidad = durabilidad
        self.daño = daño
        self.receta = None
        self.version = None

    def __str__(self) -> str:
        ''' Retorna la versión de la herramienta '''
        return str(self.version)

class HachaNormal(Hacha):
    '''
    El hacha es una herramienta que se puede utilizar para talar árboles. Se puede crear
    al comienzo del juego con 1 ramita y 1 pedernal.
    '''
    def __init__(self):
        self.durabilidad = 100
        self.daño = 27
        self.receta = {Mochila.Objetos.RAMITA: 1, Mochila.Objetos.PEDERNAL: 1}
        self.version = 'Hacha Normal'
    
class HachaLujo(Hacha):
    '''
    El Hacha de lujo es una versión del Hacha normal que tiene cuatro veces más durabilidad
    y requiere pepitas de oro en lugar de pedernal. Se necesitan 4 ramitas y 2 pepitas de oro
    para fabricar.
    '''
    def __init__(self):
        self.durabilidad = 400
        self.daño = 27
        self.receta = {Mochila.Objetos.RAMITA: 4 , Mochila.Objetos.PEPITA_ORO: 2}
        self.version = 'Hacha Lujo'

class Fogata:
    '''
    Una fogata es la clave para la supervivencia básica en el mundo. Aporta luz, calor y permite
    cocinar los alimentos. Requiere 3 césped y 2 troncos para que se pueda fabricar.
    Los personajes no pueden consumir alimentos crudos.
    '''

    def __init__(self):
        self.receta = {Mochila.Objetos.CESPED: 3, Mochila.Objetos.TRONCO: 2}
        self.version = 'Fogata'

    def __str__(self) -> str:
        ''' Retorna la versión de la herramienta '''
        return str(self.version)

    # ---------------------------------------------------------------------------------------------
    # * RETO
    # ---------------------------------------------------------------------------------------------
    # Los alimentos tienen diferentes tiempos de cocción. No queremos tener condicionales, entonces
    # usamos refactorización. Se ha comentado parte del código original.
    # Objetivo: Usar polimorfismo para obtener el tiempo de cocción y simplificar el método. Trata de
    # usar una interface con al menos los atributos: nombre, tiempo_coccion, cocido
    def cocinar(self, alimento:Alimento) -> None:
        '''
        Permite cocinar un alimento crudo en la fogata. Regresa el mismo alimento pero cocinado.
        '''        
        if alimento.cocido == False:
            sleep(alimento.tiempo_coccion)
            alimento.cocido = True

@unique
class Herramientas(Enum):
    # name = class
    HACHA_NORMAL    = 'Hacha Normal'
    HACHA_LUJO      = 'Hacha Lujo'
    MARTILLO        = 'Martillo'
    FOGATA          = 'Fogata'

    def getHerramienta(self, x):
        switcher = {
            'Martillo': Martillo(),
            'Hacha Normal': HachaNormal(),
            'Hacha Lujo': HachaLujo(),
            'Fogata': Fogata(),
        }
        return switcher.get(x,None)

class Alimento(ABC):
    def __init__(self, nombre, tiempo_coccion:int=10, cocido=False, aporte_vida=1):
        self.tiempo_coccion = tiempo_coccion
        self.cocido = cocido
        self.nombre = nombre
        self.aporte_vida = aporte_vida

    def estaCocido(self):
        ''' Retorna el estado del alimento '''
        return self.cocido

    def __str__(self) -> str:
        ''' Retorna el alimento y su estado '''        
        return self.nombre + ' ' + ('cocido' if self.estaCocido() else 'crudo')

class Cordero(Alimento):
    def __init__(self):
        self.tiempo_coccion = 3
        self.cocido = False
        self.nombre = 'Cordero'
        self.aporte_vida = 5

class Res(Alimento):
    def __init__(self):
        self.tiempo_coccion = 1
        self.cocido = False
        self.nombre = 'Res'
        self.aporte_vida = 2

@unique
class Alimentos(Enum):
    # name = class
    CORDERO = 'Cordero'
    RES     = 'Res'

    def getAlimento(self, x):
        switcher = {
            'Cordero': Cordero(),
            'Res': Res(),
        }
        return switcher.get(x,None)

if __name__ == '__main__':
    # Personajes
    wilson = Personaje('Wilson')

    # Items
    print('\n--- Creamos una mochila y añadimos trinkets')
    wilson.mochila = Mochila('Morral chico', 10)
    backpack = wilson.mochila
    trinkets = backpack.Objetos

    backpack.recoger(trinkets.RAMITA, 3)
    backpack.recoger(trinkets.ROCA, 3)
    backpack.recoger(trinkets.CUERDA)
    backpack.recoger(trinkets.CUERDA)
    backpack.recoger(trinkets.CUERDA)

    # Fabrica
    print('\n--- Fabricamos herramientas')
    backpack.fabricar(Herramientas.MARTILLO)
    backpack.fabricar(Herramientas.MARTILLO)
    backpack.recoger(trinkets.RAMITA, 3)
    backpack.recoger(trinkets.ROCA, 3)
    backpack.recoger(trinkets.CUERDA,4)
    backpack.fabricar(Herramientas.MARTILLO)

    print('\n--- Añadimos trinkets y creamos la versión inicial de un hacha')
    backpack.recoger(trinkets.RAMITA, 5)
    backpack.recoger(trinkets.PEDERNAL)
    backpack.fabricar(Herramientas.HACHA_NORMAL)

    print('\n--- Añadimos trinkets y creamos la versión de lujo de un hacha')
    backpack.recoger(trinkets.PEPITA_ORO, 2)
    backpack.fabricar(Herramientas.HACHA_LUJO)

    print(backpack)

    print('\n--- Usamos el martillo')
    backpack.demoler(trinkets.CUERDA)
    backpack.demoler(Herramientas.HACHA_LUJO)
    backpack.demoler(Herramientas.MARTILLO)
    backpack.demoler(Herramientas.MARTILLO)

    # ---------------------------------------------------------------------------------------------
    # * RETO
    # ---------------------------------------------------------------------------------------------
    # Objetivo: Agregar al menos dos alimentos que se puedan cocinar en la fogata. Crear una fogata,
    # Cocinar los alimentos en la fogata y comer los alimentos.

    print('\n--- Añadimos trinkets y creamos una fogata')
    backpack.recoger(trinkets.CESPED, 5)
    backpack.recoger(trinkets.TRONCO, 2)
    backpack.fabricar(Herramientas.FOGATA)

    print('\n--- Añadimos alimentos')
    backpack.recoger(Alimentos.RES)
    backpack.recoger(Alimentos.RES)
    backpack.recoger(Alimentos.RES)

    print('\n--- Cocinamos alimentos')
    backpack.cocinar(Alimentos.RES)
    backpack.cocinar(Alimentos.CORDERO)
    backpack.cocinar(Alimentos.RES)
    print(backpack)

    print('\n--- Comemos alimentos')
    wilson.comer(Alimentos.RES)

    # Listamos los articulos en nuestra mochila
    print(backpack)