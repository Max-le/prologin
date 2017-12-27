"""Entrée"""
M1 = 0
M2 = 0
N  = 0

""" position d'un client """
x = 0


input(M1)
input(M2)
"""1. Trouver point ou x est indifférent d'aller chez M1 ou M2."""
"""-> Point ou dist(x,M1) = dist(x,M2)
"""

"""Returne distance entre 2 points"""
def dist(a, b):
	d = 0
	d = abs(a - b)
	return d


""" x ( client ) se démarre de N = 0."""
while dist(x,M1) != dist(x,M2):

	"""le client avance"""
	x = x + 1

""" Ici le client est aussi proche de M1 que M2. (equi)"""
equi = x

""" Qui a la plus grosse ? (influence)"""
if equi > (N/2):
	winner = 1

if equi < (N/2):
	winner = 2
else:
        winner = 0

print(winner)
