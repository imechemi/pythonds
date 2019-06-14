
def toBinary(dec):
  if dec < 2:
    return str(dec)
  else:
    return toBinary(dec//2) + str(dec % 2)

print(toBinary(6))
