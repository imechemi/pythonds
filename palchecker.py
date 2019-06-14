from dequeue import Dequeue

def palchecker(str):
  d = Dequeue()

  for ch in str:
    d.addRear(ch)

  for _ in range(int(d.size()/2)):
    if (d.removeFront() != d.removeRear()):
      return False
  return True


print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
