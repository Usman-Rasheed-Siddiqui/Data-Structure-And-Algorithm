
from Lab7_exa import Stack

def InfixToPostFix(q):
    p = ""
    bodmas = ["/", "*", "+", "-"]
    q += " )"
    q = q.split()
    size = len(q)
    stack = Stack(size)
    stack.push("(")
    i = 0
    while i < size:
        element = q[i]
        if element not in "+-/^*()":
            p += q[i]

        elif element == "(":
            stack.push(element)

        elif element in "+-/^*":
            op1 = bodmas.index(element)
            for op in bodmas:
                op2 = bodmas.index(op)
                if op1 >= op2:
                    p += f"{element}"

            stack.push(element)

        elif element == ")":
            pass

