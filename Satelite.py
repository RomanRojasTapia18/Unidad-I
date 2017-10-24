"""Funcion que calcule  el satelite en orbita circular"""
import math


def satelite_orbita(G: float, M: float, r: float) -> float:
    v = math.sqrt(G * (M / r))
    return v


"""Funcion que calcule la  fuerza"""


def Fuerza(m: float, a: float) -> float:
    F = m * a
    return F
