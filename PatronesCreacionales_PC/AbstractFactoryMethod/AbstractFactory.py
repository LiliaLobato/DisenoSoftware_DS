from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum

##################################################
# Productos Abstractos
##################################################
class Silla(ABC):
  '''Clase abstracta que construir una silla'''
  def __init__(self):
    self.maxPeso = 300

  @abstractmethod
  def construir(self) -> str:
    '''Se armara la silla con todas sus partes'''
    return f'Se armó una {self} con todas sus partes'

  @abstractmethod
  def ensamblar(self) -> str:
    '''Se ensamblarán las piezas para crear una silla'''
    return f'Se ensamblarán las piezas para crear un {self}'

  @abstractmethod
  def empacar(self) -> str:
    ''' Se empacará la silla para su transporte '''
    return f'Se empacará la {self} moderno para su transporte'

  def __str__(self) -> str:
    return 'silla'

class Sofa(ABC): 
  ''' Clase abstracta para crear sofas'''
  def __init__(self):
    self.maxPeso = 500

  @abstractmethod
  def construir(self) -> str:
    '''Se armara el sofa con todas sus partes'''
    return f'Se armó una {self} con todas sus partes'

  @abstractmethod
  def ensamblar(self) -> str:
    '''Se ensamblarán las piezas para crear un sofá'''
    return f'Se ensamblarán las piezas para crear un {self}'

  @abstractmethod
  def empacar(self) -> str:
    ''' Se empacará el sofá para su transporte '''
    return f'Se empacará la {self} moderno para su transporte'

  def __str__(self) -> str:
    return 'sofa'

class Mesa(ABC):
  ''' Clase abstracta para crear mesas'''
  def __init__(self):
    self.maxPeso = 300

  @abstractmethod
  def construir(self) -> str:
    '''Se armara la mesa con todas sus partes'''
    return f'Se armó una {self} con todas sus partes'

  @abstractmethod
  def ensamblar(self) -> str:
    '''Se ensamblarán las piezas para crear una mesa'''
    return f'Se ensamblarán las piezas para crear un {self}'

  @abstractmethod
  def empacar(self) -> str:
    ''' Se empacará la mesa para su transporte '''
    return f'Se empacará la {self} moderno para su transporte'

  def __str__(self) -> str:
    return 'mesa'

##################################################
# Productos Concretos
##################################################
class SillaModerna(Silla):
  '''Clase abstracta para definir sillas con estilo moderno'''
  def __init__(self):
    self.anchura = 12
    self.largo = 8
    self.altura = 3
    self.peso = 50
    print(f'*** {self} creado... ***')

  def caerse(self) -> str:
    '''Avisa que la mesa se cayó por tener un largo X'''
    return f'La {self} se cayó por tener un largo de {self.largo}'

  def ensamblar(self) -> str:
    '''Se ensamblarán las piezas para crear una silla moderna'''
    return super().ensamblar()

  def empacar(self) -> str:
    ''' Se empacará la silla moderna para su transporte '''
    return super().empacar()

  def construir(self) -> str:
    '''Se armara la silla moderna con todas sus partes'''
    return super().construir()

  def __str__(self) -> str:
    return 'Silla moderna'
  

class MesaModerna(Mesa):
  '''Clase abstracta para definir mesas con estilo moderno'''
  def __init__(self):
    self.anchura = 6
    self.largo = 6
    self.altura = 6
    self.peso = 120
    print(f'*** {self} creado... ***')

  def caerse(self) -> str:
    '''Avisa que la mesa se cayó por tener peso mayor al máximo o por tener una altura X'''
    if(self.maxPeso > self.peso):
      return f'El {self} se cayó con un peso de {self.peso} > {self.maxPeso}'
    else:
      return f'El {self} se cayó con una altura de {self.altura}'

  def ensamblar(self) -> str:
    '''Se ensamblarán las piezas para crear una mesa moderna'''
    return super().ensamblar()

  def empacar(self) -> str:
    ''' Se empacará la mesa moderna para su transporte '''
    return super().empacar()

  def construir(self) -> str:
    '''Se armara la mesa moderna con todas sus partes'''
    return super().construir()

  def __str__(self) -> str:
    return 'mesa moderna'


class SofaModerno(Sofa):
  '''Clase abstracta para definir sofas con estilo moderno'''
  def __init__(self):
    self.anchura = 40
    self.largo = 20
    self.altura = 6
    self.peso = 230
    print(f'*** {self} creado... ***')

  def caerse(self) -> str:
    '''Avisa que la mesa se cayó por tener una anchura y largo X'''
    return f'El {self} se cayó por tener una anchura de {self.anchura} y un largo de {self.largo}'

  def ensamblar(self) -> str:
    '''Se ensamblarán las piezas para crear una sofa moderno'''
    return super().ensamblar()

  def empacar(self) -> str:
    ''' Se empacará la sofa moderno para su transporte '''
    return super().empacar()

  def construir(self) -> str:
    '''Se armara la sofa moderno con todas sus partes'''
    return super().construir()

  def __str__(self) -> str:
    return 'sofa moderno'


class SofaContemporaneo(Sofa):
  '''Clase abstracta para definir sofas con estilo contemporaneo'''
  def __init__(self):
    self.anchura = 15
    self.largo = 9
    self.altura = 3
    self.peso = 53
    print(f'*** {self} creado... ***')

  def ensamblar(self) -> str:
    '''Se ensamblarán las piezas para crear una sofa contemporaneo'''
    return super().ensamblar()

  def empacar(self) -> str:
    ''' Se empacará la sofa contemporaneo para su transporte '''
    return super().empacar()

  def construir(self) -> str:
    '''Se armara la sofa contemporaneo con todas sus partes'''
    return super().construir()

  def __str__(self)-> str:
    return 'sofa contemporanea'

class SillaContemporanea(Silla):
  '''Clase abstracta para definir sillas con estilo contemporaneo'''
  def __init__(self):
    self.anchura = 6
    self.largo = 8
    self.altura = 15
    self.peso = 120
    print(f'*** {self} creado... ***')
   
  def caerse(self) -> str:
    '''Avisa que la mesa se cayó por tener un asiento X'''
    return f'La {self} se cayó por tener un asiento de {self.largo} x {self.anchura}'

  def ensamblar(self) -> str:
    '''Se ensamblarán las piezas para crear una silla contemporanea'''
    return super().ensamblar()

  def empacar(self) -> str:
    ''' Se empacará la silla contemporanea para su transporte '''
    return super().empacar()

  def construir(self) -> str:
    '''Se armara la silla contemporanea con todas sus partes'''
    return super().construir()

  def __str__(self)-> str:
    return 'silla contemporanea'


class MesaContemporanea(Mesa):
  '''Clase abstracta para definir mesas con estilo contemporaneo'''
  def __init__(self):
    self.anchura = 40
    self.largo = 20
    self.altura = 60
    self.peso = 270
    print(f'*** {self} creado... ***')

  def caerse(self) -> str:    
    '''Avisa que la mesa se cayó por tener un peso mayor al peso máximo o un peso X * 2.78'''
    if(self.maxPeso > self.peso):
      return f'El {self} se cayó con un peso de {self.peso} > {self.maxPeso}'
    else:
      return f'El {self} se cayó con un peso de {self.peso * 2.78}'      

  def ensamblar(self) -> str:
    '''Se ensamblarán las piezas para crear una mesa contemporanea'''
    return super().ensamblar()

  def empacar(self) -> str:
    ''' Se empacará la mesa contemporanea para su transporte '''
    return super().empacar()

  def construir(self) -> str:
    '''Se armara la mesa contemporanea con todas sus partes'''
    return super().construir()

  def __str__(self)-> str:
    return 'mesa contemporanea'


##################################################
# Interfase de la fábrica
##################################################
class MueblesIteso(ABC):
  @abstractmethod
  def crear_mesa(self) -> None:
    '''crea una mesa de algun estilo'''
    pass
		
  @abstractmethod
  def crear_silla(self) -> None:
    '''crea una silla de algun estilo'''
    pass
		
  @abstractmethod
  def crear_sofa(self) -> None:
    '''crea un sofa de algun estilo'''
    pass
    

##################################################
# Fabricas concretas
##################################################
class Modernos(MueblesIteso):
  def crear_mesa(self) -> Mesa:
    '''crea una mesa de algun estilo'''
    return MesaModerna()

  def crear_silla(self) -> Silla:
    '''crea una silla de algun estilo'''
    return SillaModerna()

  def crear_sofa(self) -> Sofa:
    '''crea un sofa de algun estilo'''
    return SofaModerno()

class Contemporaneos(MueblesIteso):
  def crear_mesa(self) -> Mesa:
    '''Crea una mesa contemporanea'''
    return MesaContemporanea()
		
  def crear_silla(self) -> Silla:
    '''Crea una silla contemporanea'''
    return SillaContemporanea()
		
  def crear_sofa(self) -> Sofa:
    '''Crea un sofa contemporaneo'''
    return SofaContemporaneo()
    
##################################################
# Clase Auxiliar para clientes
##################################################
class Client:
    class TipoEstilo(Enum):
        # name          value  
        CONTEMPORANEO    = Contemporaneos()
        MODERNO          = Modernos()
    
    @staticmethod 
    def crear(tipo: TipoEstilo) -> MueblesIteso:
        ''' Crea un nuevo estilo de muebles'''
        return tipo.value

##################################################
# Consumo de código
##################################################
if __name__ == '__main__':
  sucursalModerna = Client.crear(Client.TipoEstilo.MODERNO)
  sucursalContemporaneo = Client.crear(Client.TipoEstilo.CONTEMPORANEO)

  print('\nMuebles Modernos')
  print(sucursalModerna.crear_sofa().ensamblar())
  print(sucursalModerna.crear_mesa().empacar())
  print(sucursalModerna.crear_silla().construir())

  print('\nMuebles Contemporaneos')
  print(sucursalContemporaneo.crear_sofa().empacar())
  print(sucursalContemporaneo.crear_mesa().ensamblar())
  print(sucursalContemporaneo.crear_silla().caerse())