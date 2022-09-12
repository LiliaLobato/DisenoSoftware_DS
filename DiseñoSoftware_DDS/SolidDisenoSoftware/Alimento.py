from __future__ import annotations
from Menu import Menu

class Alimento(Menu):
    def getDescripcion(self) -> str:
      ''' Retorna la descripcion de un alimento '''
      return 'Descripción de Alimento: {}'.format(self.descripcion)


class Chilaquil(Alimento):
    def __init__(self):
      self.descripcion = 'Chilaquiles rojos con pollo'
      self.precio = 50

class Huevo(Alimento):
    def __init__(self):
      self.descripcion = 'Dos huevos revuelto/estrellado '
      self.precio = 32
