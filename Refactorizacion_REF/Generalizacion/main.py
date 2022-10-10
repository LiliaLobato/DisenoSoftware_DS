from __future__ import annotations
from Comensal import Comensal
from Mesa import Mesa
import Postre
import Alimento
import Bebida

# Probamos clases e interfaces  
# UML: https://drive.google.com/file/d/1u9bgaEUjlpd9Rgzp6DFpv67WAMZDg_3c/view?usp=sharing

print('-- MENU --')
print(Postre.Pastel())
print(Alimento.Chilaquil())
print(Bebida.Cafe())

print('\n-- CUENTAS POR CLIENTE --')
comensal_1 = Comensal("Carla")
comensal_1.addComida(Postre.Pastel())
print(comensal_1)
  
comensal_2 = Comensal("Alfonso")
comensal_2.addComida(Alimento.Chilaquil())
comensal_2.addComida(Bebida.Cafe())
print(comensal_2)

comensal_3 = Comensal("David")
comensal_3.addComida(Alimento.Huevo())
comensal_3.addComida(Postre.Pastel())
print(comensal_3)

print('\n-- CUENTAS POR MESA --')
mesa_1 = Mesa(1)
mesa_1.addComensal(comensal_1)
mesa_1.addComensal(comensal_2)
print(mesa_1)

mesa_2 = Mesa(2)
mesa_2.addComensal(comensal_3)
print(mesa_2)