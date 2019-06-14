def reverse(st):
  if len(st) == 1:
    return st[0]
  else:
    return reverse(st[1:]) + st[0]


print(reverse("abcdefg"))
