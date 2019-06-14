
def listSum(arr):
  if len(arr) == 1:
    return arr[0]
  else:
    return arr[0] + listSum(arr[1:])


numlist = [8, 2, 1, 4, 4]


print(listSum(numlist))
