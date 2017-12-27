"""Entrée"""
M1 = 50
M2 = 250
N  = 500
"""AIRE ENTRE M1 ET M2 = (M2-M1)"""

"""Aire de M1"""
AM1 = M1+((M2-M1)/2)

"""Aire de M2"""
AM2 = N - M2  +((M2-M1)/2)

winner = 0
if AM2 < AM1:
	winner = 1
elif AM2 == AM1:
	winner = 0
else:
	print("Error.")
print(AM1)
print(AM2)
print(winner)
