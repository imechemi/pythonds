class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

  def getNext(self):
    return self.next

  def getData(self):
    return self.data

  def setNext(self, nextNode):
    self.next = nextNode


class UnorderedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def add(self, data):
    newnode = Node(data)
    newnode.setNext(self.head)
    if self.head == None:
      self.tail = newnode
    else:
      self.tail = self.head
    self.head = newnode


  def append(self, data):
    newnode = Node(data)
    self.tail.setNext(newnode)
    self.tail = newnode

  def search(self, item):
    current = self.head
    found = False
    while current != None and not found:
      if current.getData() == item:
        found = True
      else:
        current = current.getNext()

    return True if found else False

  def show(self):
    current = self.head
    while current != None:
      print(current.data, end=" | ")
      current = current.next
    print("\n")

  def remove(self, item):
    current = self.head
    previous = None

    found = False
    while current != None and not found:
      if current.getData() == item:
        found = True
        if previous == None:
          self.head = None
        else:
          previous.setNext(current.getNext())
        return current.getData()
      else:
        previous = current
        current = current.getNext()

  def index(self, item):
    i = 0
    current = self.head
    found = False
    while current != None and not found:
      if (current.getData() == item):
        found = True
      current = current.getNext()
      i += 1
    return i-1

  def insert(self, pos, item):
    i = 0
    current = self.head
    previous = None
    while current != None:
      if (i == pos):
        break
      previous = current
      current = current.getNext()
      i += 1

    newnode = Node(item)
    if previous == None:
      self.head = newnode
    else:
      newnode.setNext(current)
      previous.setNext(newnode)

  def size(self):
    curr = self.head
    ct = 0
    while curr != None:
      ct += 1
      curr = curr.getNext()
    return ct

  def isEmpty(self):
    return self.head == None

  def pop(self):
    if self.isEmpty():
      return

    curr = self.head
    prev = None
    while curr.next != None:
      prev = curr
      curr = curr.getNext()
    if prev != None:
      prev.setNext(None)

  def popPos(self, pos):
    if self.isEmpty():
      return -1

    i = 0
    curr = self.head
    prev = None
    found = False
    while curr != None and not found:
      if i == pos:
        found = True
      else:
        prev = curr
        curr = curr.getNext()
      i += 1

    if not found:
      return -1
    else:
      if prev == None:
        self.head = None
      else:
        prev.setNext(curr.getNext())
      return curr.getData()


ulist = UnorderedList()
ulist.add(5)
ulist.add(6)
ulist.append(4)
ulist.show()

ulist.add(3)
ulist.add(7)
ulist.add(8)
ulist.add(32)
ulist.add(2)
ulist.show()

print(ulist.remove(8))
ulist.show()

ulist.append(20)
ulist.add(13)
ulist.show()

print(ulist.index(20))
ulist.insert(2, 67)
ulist.show()

print(ulist.size())
print(ulist.isEmpty())
ulist.show()

ulist.pop()
ulist.show()

print(ulist.popPos(2))
ulist.show()
