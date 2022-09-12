from __future__ import annotations
from Menu import Menu

class Bebida(Menu):
  def getDescripcion(self) -> str:
    ''' Retorna la descripcion de una bebida '''
    return 'Descripción de Bebida: {}'.format(self.descripcion)

class Cafe(Bebida):
  def __init__(self):
    self.descripcion = "Cafe de olla calientito"
    self.precio = 20.0



  
    
    
  