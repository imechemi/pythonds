import timeit
import random

for i in range(10000, 1000001,20000):
  x_lst = [x for x in range(i)]
  x_dict = {j:1 for j in range(i)}
  t1 = timeit.Timer("del(x_lst[%d])"%(i/2), "from __main__ import x_lst")
  t2 = timeit.Timer("del x_dict[%d]"%(i), "from __main__ import x_dict")
  
  print(t1.timeit(number=0))
  print(t2.timeit(number=0))
