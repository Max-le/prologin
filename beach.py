"""Entrée"""
M1 = 0
M2 = 0
N  = 0

""" position d'un client """
x = 0

"""1. Trouver point ou x est indifférent d'aller chez M1 ou M2."""
"""-> Point ou dist(x,M1) = dist(x,M2)
"""

"""Returne distance entre 2 points"""
def dist(a, b):
	d = 0
	d = abs(a - b)
	return d

