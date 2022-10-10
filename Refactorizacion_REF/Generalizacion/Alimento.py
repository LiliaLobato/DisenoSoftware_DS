from __future__ import annotations
from Menu import Menu

class Alimento(Menu):
  # Pull up Field
  def __init__(self, descripcion, precio):
    super().__init__(descripcion, precio)

class Chilaquil(Alimento):
    def __init__(self):
      super().__init__('Chilaquiles rojos con pollo', 50)

class Huevo(Alimento):
    def __init__(self):
      super().__init__('Dos huevos revuelto/estrellado', 32)
