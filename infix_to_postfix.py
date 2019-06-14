import stack
from stack import Stack


def prec(operator):
  precedence = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    ')': 3
  }
  return precedence[operator]


def infix_to_postfix(infix):
  opstack = Stack()
  exprlst = list(infix)
  postfix = ''
  for token in exprlst:
    if token == '(':
      opstack.push(token)
    elif token in '+-/*':
      while not opstack.isempty() and prec(token) < prec(opstack.peek()):
        postfix += opstack.pop()
      opstack.push(token)
    else:
      if token == ')':
        while not opstack.isempty() and opstack.peek() != '(':
          postfix += opstack.pop()
        opstack.pop()
      else:
        postfix += token

  while not opstack.isempty():
    postfix += opstack.pop()
  
  return postfix


print(infix_to_postfix("A+B*C"))
print(infix_to_postfix("A*B+C*D"))
print(infix_to_postfix("(A+B)*C-(D-E)*(F+G)"))