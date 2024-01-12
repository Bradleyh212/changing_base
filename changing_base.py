def base_10_to_2(n):
	h = int(n)
	l = []
	while h > 0:
		l.append(h%2)
		h = h//2
	return l[::-1]

p = base_10_to_2(24)
print(p)


def base_10_to_8(n):
	h = int(n)
	l = []
	while h > 0:
		l.append(h%8)
		h = h//8
	return l[::-1]

p = base_10_to_8(73)
print(p)


def base_10_to_16(n):
	h = int(n)
	l = []
	while h > 0:
		l.append(h%16)
		h = h//16


	return l[::-1]

p = base_10_to_16(73.4)
print(p)

