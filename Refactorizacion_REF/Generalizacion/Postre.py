from __future__ import annotations
from Menu import Menu

class Postre(Menu):
  # Pull up Field
  def __init__(self, descripcion, precio):
    super().__init__(descripcion, precio)

class Pastel(Postre):
  def __init__(self):
    super().__init__("Pastel de tres leches", 30)

  