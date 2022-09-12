from __future__ import annotations
from abc import ABC

#Menu Interface
class Menu(ABC):

    def __init__(self, descripcion:str, precio:int):
      self.descripcion = descripcion
      self.precio = precio
    
    def __str__(self) -> str:
      ''' Retorna la descripcion como string'''
      return self.getDescripcion()

    def getDescripcion(self) -> str:
      ''' Retorna la descripcion '''
      return 'Descripción: {}'.format(self.descripcion)

    def getPrecio(self) -> float:
      ''' Retorna el precio '''
      return self.precio
