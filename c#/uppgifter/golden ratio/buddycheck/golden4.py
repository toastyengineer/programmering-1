from decimal import *
getcontext().prec = 29
GOLDEN = 1.61803398874989484820458683436
NUMBERS = 100
f = []
f.append(Decimal(0))
f.append(Decimal(1))
for i in range(2, NUMBERS+1):
	f.append(f[i-2]+f[i-1])
	if f[-1]/f[-2] == GOLDEN:
		break
print(f[-1]/f[-2])
