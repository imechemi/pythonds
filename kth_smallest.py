def kthsmallest_bysort(arr, k):
  clist = arr.copy()
  clist.sort()
  cset = set(clist)
  clist = list(cset)
  return clist[k-1]


def kthsmallest(arr, k):
  prevsmallest = 0

  for _ in range(k - 1):
    smallest = arr[0]
    for i in range(len(arr)):
      if arr[i] > prevsmallest:
        smallest = arr[i]
      
    prevsmallest = smallest
  return smallest




nlist = [5, 0, 2, 3, 5, 3, 0, 8, 9, 7]

# kthsmallest(nlist, 1)
# kthsmallest(nlist, 2)
print(kthsmallest(nlist, 2))
print(kthsmallest(nlist, 3))
print(kthsmallest(nlist, 4))
print(kthsmallest(nlist, 5))

# print(kthsmallest(nlist, 3) == 3)
# print(kthsmallest(nlist, 4) == 5)
# print(kthsmallest(nlist, 5) == 7)