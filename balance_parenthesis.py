import stack 
from stack import Stack 

def matches(top, sym):
  closings = "([{"
  openings = ")]}"

  if sym == openings[(closings.index(top))]:
    return True 
  else:
    return False 


def parChecker(symbolString):
  st = Stack()
  balanced = True
  for sym in symbolString:
    if sym in '([{':
      st.push(sym)
    else:
      if st.isempty():
        balanced = False
        break
      else:
        top = st.pop()
        if not matches(top, sym):
          balanced = False
          break

  if st.isempty() and balanced:
    return True
  else:
    return False 



print(parChecker('(())(((()())))'))
print(parChecker('(())(((()()))'))
print(parChecker('((()))'))
print(parChecker('(()'))
print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))