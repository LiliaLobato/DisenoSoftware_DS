# DISEÑO DE SOFTWARE
# MODULO 4 - PATRONES DE DISEÑO
# FACTORY METHOD SESIÓN PRÁCTICA
# 29 DE SEPTIEMBRE 2022

from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum


# 1.- Interface para productos
class Prueba(ABC):
  ''' Interfaz común para Prueba '''

  def ejecutar(self) -> str:
    ''' Método que ejecuta la prueba'''
    return 'Ejecutando '

  def pausar(self) -> str:
    ''' Metodo para pausar la prueba'''
    return 'Pausando '

  def detener(self) -> str:
    ''' Metodo para detener la prueba'''
    return 'Deteniendo '


# 2.- Productos Concretos
class Estres(Prueba):
  '''Clase concreta estrés'''

  def ejecutar(self) -> str:
    '''Retorna la prueba que se está ejecutando'''
    return super().ejecutar() + ' prueba de estrés'

  def pausar(self) -> str:
    '''Retorna un string indicando la pausa de la prueba'''
    return super().pausar() + 'prueba de estrés'

  def detener(self) -> str:
    '''Retorna un string indicando la pausa de la prueba'''
    return super().pausar() + 'prueba de estrés'


class Memoria(Prueba):
  '''Clase concreta memoria'''

  def ejecutar(self) -> str:
    '''Retorna la prueba que se esta ejecutando'''
    return super().ejecutar() + 'prueba de memoria'

  def pausar(self) -> str:
    '''Retorna un string de pausar la prueba de memoria'''
    return super().pausar() + 'prueba de memoria'

  def detener(self) -> str:
    '''Retorna un string indicando la pausa de la prueba'''
    return super().pausar() + 'prueba de memoria'


class Power(Prueba):
  '''Clase concreta power'''

  def ejecutar(self) -> str:
    '''Retorna un string de ejecución de la prueba de power'''
    return super().ejecutar() + 'prueba de power'

  def pausar(self) -> str:
    '''Retorna un string de pausar la prueba de power'''
    return super().pausar() + 'prueba de power'

  def detener(self) -> str:
    '''Retorna un string indicando la pausa de la prueba'''
    return super().pausar() + 'prueba de power'


class Concurrencia(Prueba):
  '''Clase concreta concurrencia '''

  def ejecutar(self) -> str:
    ''' Retorna la prueba que se esta ejectuando '''
    return super().ejecutar() + 'prueba de concurrencia'

  def pausar(self) -> str:
    '''Retorna un str de pausa para la prueba de concurrencia'''
    return super().pausar() + 'prueba de concurrencia'

  def detener(self) -> str:
    '''Retorna un string indicando la pausa de la prueba'''
    return super().pausar() + 'prueba de concurrencia'


# 3.- Factory (Clase creadora)
class DiseñoTech():

  def realizar_prueba(self, tipoPrueba: Pruebas) -> object:
    '''Relizar una nueva prueba'''
    return tipoPrueba.value

  def ejecutar(self, tipo: Pruebas) -> str:
    ''' Retorna la prueba que se esta ejectuando '''
    return self.realizar_prueba(tipo).ejecutar()

  def pausar(self, tipo: Pruebas) -> str:
    '''Pausar una prueba'''
    return self.realizar_prueba(tipo).pausar()

  def detener(self, tipo: Pruebas) -> str:
    '''Detiene prueba'''
    return self.realizar_prueba(tipo).detener()


# 4.- Fabricas concretas
class Pruebas(ABC):
  ''' Superclase para todas las pruebas '''
  pass


class Nvidia(DiseñoTech, Pruebas):

  class TipoPrueba(Enum):
    #name    value
    ESTRES = Estres()
    POWER = Power()


class Samsung(DiseñoTech, Pruebas):

  class TipoPrueba(Enum):
    #name    value
    ESTRES = Estres()
    MEMORIA = Memoria()
    CONCURRENCIA = Concurrencia()
    POWER = Power()


class Intel(DiseñoTech, Pruebas):

  class TipoPrueba(Enum):
    # name   value
    CONCURRENCIA = Concurrencia()


if __name__ == '__main__':
  tester = Intel()
  prueba1 = tester.realizar_prueba(tester.TipoPrueba.CONCURRENCIA)
  print(prueba1.ejecutar())
