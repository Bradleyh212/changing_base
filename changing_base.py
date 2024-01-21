import math

def base_10_to_2(n):
	whole_n = int(n)
	binary_int = []
	binary_dec = []
	if n > 0:
		dec_n = n - whole_n


	while whole_n > 0:
		binary_int.append(whole_n % 2)
		whole_n //= 2
	binary_int = binary_int[::-1]

	while dec_n > 0:
		dec_n *= 2
		int_n = int(dec_n)
		binary_dec.append(int_n)
		dec_n -= int_n

	whole_binary = binary_int + binary_dec

	return whole_binary




def base_10_to_8(n):
	h = int(n)
	l = []
	while h > 0:
		l.append(h%8)
		h = h//8
	return l[::-1]



def base_10_to_16(n):
	h = int(n)
	l = []
	while h > 0:
		l.append(h%16)
		h = h//16


	return l[::-1]




