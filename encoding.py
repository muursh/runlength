# run length encoding

def encode(orig):
	if orig == "":
		return ""
	else:
		final = orig[0]
		orig_length = len(orig)
		i = 1
		while i < orig_length and final == orig[i]:
			i += 1
		return final + str(i) + encode(orig[i:])

print(encode("engineering"))
