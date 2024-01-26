# Name: Bradley-Hans Desmornes 
# Name : Mathew Al-Frenn
# year 2024

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

	whole_binary = binary_int + ["."] + binary_dec

	string_whole_binary = ""
	for i in whole_binary:
		string_whole_binary += str(i)
		
	return string_whole_binary


def base_10_to_8(n):
	whole_n = int(n)
	octal_int = []
	octal_dec = []
	if n > 0:
		dec_n = n - whole_n

	while whole_n > 0:
		octal_int.append(whole_n % 8)
		whole_n //= 8
	octal_int = octal_int[::-1]

	while dec_n > 0:
		dec_n *= 8
		int_n = int(dec_n)	
		octal_dec.append(int_n)
		dec_n -= int_n

	whole_octal = octal_int + ["."] + octal_dec

	string_whole_octal = ""
	for i in whole_octal:
		string_whole_octal += str(i)

	return string_whole_octal


def base_10_to_16(n):
	whole_n = int(n)
	hexa_int = []
	heax_dec = []
	if n > 0:
		dec_n = n - whole_n

	while whole_n > 0:
		hexa_int.append(whole_n % 16)
		whole_n //= 16
	hexa_int = hexa_int[::-1]

	while dec_n > 0:
		dec_n *= 16
		int_n = int(dec_n)	
		heax_dec.append(int_n)
		dec_n -= int_n

	whole_hexa = hexa_int + ["."] + heax_dec

	string_whole_hexa = ""
	for i in whole_hexa:
		string_whole_hexa += str(i)

	return string_whole_hexa




