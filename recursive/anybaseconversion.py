
def convert(num, base):
  print(num, base)
  lookup = "0123456789ABCDEF"
  if num < base:
    return str(lookup[num])
  else:
    return convert((num // base), base) + str(lookup[num % base])

print(convert(255, 2))
