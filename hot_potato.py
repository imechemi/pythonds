import queue 
from queue import Queue 

def hotPotato(name_list, num):
  names = Queue()
  for name in name_list:
    names.enqueue(name)

  while names.size() > 1:
    for _ in range(num):
      names.enqueue(names.dequeue())
    print(names)
    out = names.dequeue()
    print(out, "is out")

  print(names)


hotPotato(['Chemi', 'Tamstin', 'Tennor', 'Tsetan'], 5)