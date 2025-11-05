
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

def InfixToPostFix(q):
    p = ""
    q += " )"
    q = q.split()

    size = len(q)
    stack = Stack(size)
    stack.push("(")

    for element in q:
        if element not in "+-/^*()":
            p += f"{element} "

        elif element == "(":
            stack.push(element)

        elif element in "+-*/^":
            while True:
                top1 = stack.top()
                if precedence(top1) >= precedence(element):
                    p += f"{stack.pop()} "
                
                else:
                    break

            stack.push(element)

        elif element == ")":
            while True:
                tmp = stack.pop()
                if tmp == "(":
                    break
                p += f"{tmp} "

    return p

q = "( 8 + 2 ) * ( 6 - 3 ) / ( 4 + 1 )"
p = InfixToPostFix(q)
print("Result of PostFix:", p)

