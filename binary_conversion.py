from stack import Stack

ch = input("Enter number: ")

while ch != '':
  st = Stack()
  n = int(ch)
  while (n > 0):
    rem = n % 2
    n = n / 2
    st.push(rem)

  binary = ""
  while not st.isempty():
    binary += str(st.pop())
  print(binary)

  ch = input("Enter number: ")
