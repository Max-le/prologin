"""Entrée"""
M1 = 50
M2 = 250
N  = 500

""" position d'un client """
x = 0

"""1. Trouver point ou x est indifférent d'aller chez M1 ou M2."""
"""-> Point ou dist(x,M1) = dist(x,M2)
"""



""" x ( client ) se démarre de N = 0."""
while abs(M1-x) != abs(M2-x):

	"""le client avance"""
	x = x + 1
	

""" Ici le client est aussi proche de M1 que M2. (equi)"""
equi = x
print("equi= " , equi)

""" Qui a la plus grosse ? (influence)"""
print(N/2)
if equi > N/2:
	winner = 1

elif equi < N/2:
	winner = 2
else :
        winner = 0
        
print(winner)
