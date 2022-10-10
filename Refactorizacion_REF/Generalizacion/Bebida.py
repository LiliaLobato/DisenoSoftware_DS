from __future__ import annotations
from Menu import Menu

class Bebida(Menu):  
  # Pull up Field
  def __init__(self, descripcion, precio):
    super().__init__(descripcion, precio)

class Cafe(Bebida):
  def __init__(self):
    super().__init__("Cafe de olla calientito", 20)



  
    
    
  