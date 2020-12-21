def binary_to_dec(binary):
  exponent = 0
  total = 0
  for i in range(len(binary)):
    total += int(binary[-i-1]) * (2 ** (exponent))
  return total
def dec_to_binary(dec):
  