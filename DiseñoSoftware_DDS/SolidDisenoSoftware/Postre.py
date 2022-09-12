from __future__ import annotations
from Menu import Menu

class Postre(Menu):
    def getDescripcion(self) -> str:
      ''' Retorna la descripcion de un postre '''
      return 'Descripción del Postre: {}'.format(self.descripcion)

class Pastel(Postre):
  def __init__(self):
    self.descripcion = "Pastel de tres leches"
    self.precio = 30

  