from Stack import Stack

def precedence(op):
    if op == "^":
        return 3
    
    elif op in "*/":
        return 2
    
    elif op in "+-":
        return 1
    
    else:
        return 0


def operator(op, operatorStack, operandStack):
    if op == "(":
        operatorStack.push(op)
        return operatorStack, operandStack
    
    elif op == ")":
        while operatorStack.top() != "(":
            topOp = operatorStack.pop()
            Operand2 = operandStack.pop()
            Operand1 = operandStack.pop()
            operation = eval(str(Operand1) + 
            ('**' if topOp == '^' else topOp) + str(Operand2) )
            operandStack.push(operation)
        operatorStack.pop()
        return operatorStack, operandStack
        
    else:
        while not operatorStack.isEmpty() and \
        precedence(op) <= precedence(operatorStack.top()) \
        and operatorStack.top() != "(":

            topOp = operatorStack.pop()
            Operand2 = int(operandStack.pop())
            Operand1 = int(operandStack.pop())
            operation = eval(str(Operand1) +
            ('**' if topOp == '^' else topOp) + str(Operand2) )
            operandStack.push(operation)
            
        operatorStack.push(op)
        return operatorStack, operandStack

def EvalInfix(q):
    q = q.split()
    size = len(q)
    operatorStack = Stack(size)
    operandStack = Stack(size)

    operatorStack.push("(")
    q.append(")")

    for value in q:
        if value not in "+-/^*()":
            operandStack.push(value)

        else:
            operatorStack, operandStack = \
            operator(value, operatorStack, operandStack)

    return operandStack.pop()

q = "( 8 + 2 ) * ( 6 - 3 ) / ( 4 + 1 )"
result = EvalInfix(q)
print("Result:", result)





