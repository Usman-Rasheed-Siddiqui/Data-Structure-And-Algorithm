
from Stack import Stack

def EvalPostFix(p):
    p += " )"
    p = p.split()
    size = len(p)
    stack = Stack(size)
    i = 0
    while i < size:
        element = p[i]
        if element not in "+-/^*()":
            stack.push(int(element))

        elif element == ")":
            return stack.top()

        else:
            t = stack.pop()
            nt = stack.pop()
            result = int(eval(str(nt) + ("**" if element=="^" else element) + str(t)))
            stack.push(result)

        i += 1



expression = "1 4 18 6 / 3 + + 5 / +"
result = EvalPostFix(expression)
print("Result of PostFix:", result)






