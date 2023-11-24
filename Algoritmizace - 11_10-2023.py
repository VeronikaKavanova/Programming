from math import sqrt

def prvocislo(n):
	# prověříme všechny dělitele
	for d in range(2,int(sqrt(n))+1):
		if n % d == 0: 
			return False 
	return True

print(prvocislo(2147483647))