from __future__ import annotations
import Menu

class Comensal:
    def __init__(self, name:str, pedido:list = []):
        self.pedido = []
        self.name = name
    
    def __str__(self) -> str:
      ''' Retorna la informaicon de un comensal y su total a pagar'''
      return "Comensal: " + str(self.name) + "\n\t Productos: " + str(len(self.pedido)) + "\n\t Total: $" + str(self.getCuentaPersonal())
    
    def addComida(self, pedido:Menu) -> None:
      ''' Añade un alimento a la orden del comensal si es parte del menu '''
      if(isinstance(pedido, Menu.Menu)):
        self.pedido.append(pedido)
    
    def getCuentaPersonal(self) -> float:      
      ''' Retorna la cuenta del comensal '''
      cuenta = 0
      for pedido in self.pedido:
        cuenta += pedido.precio
      return cuenta
