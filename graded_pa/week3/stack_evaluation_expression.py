# A postfix expression can be evaluated with a stack using the following algorithm:
# Create a stack to store operands (or numbers).
# Scan each element in the given expression left to right.
# If the element is a number (operand), push it into the stack.
# If the element is an operator, pop two operands (Assume that the first popped element is B and the second popped element is A) for the operator op from the stack. Evaluate the operation (A op B) and push the result back to the stack.
# When the expression ends, the number in the stack is the final answer.
# Write a function EvaluateExpression(exp), that accepts an expression exp in string format, where each item is separated by the space. The function returns the evaluated value.

class create_stack:
  def __init__(self):
    self.stack = []
  def push(self,d):
    self.stack += [d]
  def pop(self):
    t = self.stack[-1]
    self.stack = self.stack[:-1]
    return t

def EvaluateExpression(exp):
  opt = ['+','-','*','/','**']
  stk = create_stack()
  L = exp.split(' ')
  for i in L:
    if i not in opt:
      stk.push(i)
    else:
      b = stk.pop()
      a = stk.pop()
      res = eval(a + i + b)
      stk.push(str(res))
  return stk.pop()
print(float(EvaluateExpression(input())))