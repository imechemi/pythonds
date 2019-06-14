import stack 
from stack import Stack 

def baseconvert(number, base):
  digits = '0123456789ABCDEF'
  st = Stack()
  while(number > 0):
    rem = number % base
    st.push(rem)
    number = number // base
  
  binstr=''
  while not st.isempty():
    binstr = binstr + digits[st.pop()]
  return binstr 

print(baseconvert(25, 8))