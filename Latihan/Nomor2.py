print("---Formasi ke satu---")
def starFormation(n):
	i = 0
	while i <= n:
		kol = i
		while kol > 0:
			print('*', end=' ')
			kol -= 1
		i += 1
		print()

starFormation(4)

print("---Formasi ke dua---")
def starFormation2(n):
	i = 1
	while i <= n:
		kol = n
		while kol >= i:
			print('*', end=' ')
			kol -= 1
		i += 1
		print()

starFormation2(4)

print("---Formasi Gabungan---")
def starFormation3(n):
	i = 0
	while i <= n:
		if i <= n/2:
			i = 0
			while i <= n/2:
				kol = i
				while kol > 0:
					print('*', end=' ')
					kol -= 1
				i += 1
				print()
		elif i >= n/2:
			i = 0
			while i <= n:
				kol = n/2
				while kol >= i:
					print('*', end=' ')
					kol -= 1
				i += 1
				print()
		i += 1

starFormation3(10)