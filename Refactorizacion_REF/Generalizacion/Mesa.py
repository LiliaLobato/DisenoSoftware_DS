from __future__ import annotations
import Comensal


class Mesa():

    def __init__(self, numero:int, comensales:Comensal = []):
        self.numero = numero
        self.comensales = []

    def __str__(self) -> str:
      ''' Retorna la informaicon de una mesa y su total a pagar'''
      return "Mesa: " + str(self.numero) + "\n\t Comensales: " + str(len(
          self.comensales)) + "\n\t Total: $" + str(self.getCuenta())

    def getCuenta(self) -> float:
      ''' Retorna la cuenta de la mesa '''
      cuenta = 0
      for cliente in self.comensales:
        cuenta += cliente.getCuentaPersonal()
      return cuenta

    def addComensal(self, comensal: Comensal) -> None:
      ''' Añade un comensal a la mesa '''
      if(isinstance(comensal, Comensal.Comensal)):
        self.comensales.append(comensal)
