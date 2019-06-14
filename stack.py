class Stack:

  def __init__(self):
    self.items = []

  def isempty(self): 
    return self.items == []

  def pop(self):
    return self.items.pop()
  
  def push(self, item):
    self.items.append(item)

  def peek(self):
    return self.items[len(self.items) - 1]

  def __str__(self):
    res = ''
    for item in self.items: 
      res = res + str(item) + ' '
    
    return res 


def revstring(name):
  st = Stack()
  for i in name:
    st.push(i)
    
  res = ''
  while(not st.isempty()):
    res = res + st.peek()
    st.pop()

  return res


# print(revstring("tenzin chemi"))



