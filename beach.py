# Petit programme pour calculer si M1 ou M2 a le plus d'influence sur la plage.


"""Entrée"""

M1 = float(input())
M2 = float(input())
N  = float(input())

"""AIRE ENTRE M1 ET M2 = (M2-M1)"""

"""Aire de M1"""
AM1 = M1+((M2-M1)/2)

"""Aire de M2"""
AM2 = N - M2  +((M2-M1)/2)

winner = 5
if AM2 < AM1:
	winner = 1
elif AM2 > AM1:
	winner = 2
elif AM1 == AM2:
	winner = 0
else:
	print("Something went wrong..")

print(winner)
