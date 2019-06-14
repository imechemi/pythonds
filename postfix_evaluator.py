import stack
from stack import Stack 

def calculate(op1, op2, operator):
  if operator == '-':
    return op1 - op2 
  elif operator == '+':
    return op1 + op2
  elif operator == '*':
    return op1 * op2 
  elif operator == '/':
    return op1 / op2
  
def evaluate_postfix(postfix):
  operand_stack = Stack()
  expr_list = list(postfix)

  for token in expr_list:
    if token in '+-*/':
      op2 = operand_stack.pop()
      op1 = operand_stack.pop()
      res = calculate(op1, op2, token)
      operand_stack.push(res)
    else:
      operand_stack.push(int(token))
  
  print(operand_stack)
    

evaluate_postfix('456*+')
evaluate_postfix('78+32+/')