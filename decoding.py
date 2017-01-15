def decode(orig):
	if not orig:
		return ""
	else:
		char = orig[0]
		amount = orig[1]
		return char * int(amount) + decode(orig[2:])

print(decode("m1u2r1s1h1"))
