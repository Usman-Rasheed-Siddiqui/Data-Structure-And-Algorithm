

class Stack:
    def __init__(self, maxstk):
        self.stack = []
        self.maxstk = maxstk
        self.tos = -1

    def get_info(self):
        print(self.stack, self.tos)

    def pop(self):
        if self.tos == -1:
            print("Underflow!")
            return
        else:
            temp = self.stack.pop()
            self.tos -= 1
            return temp

    def push(self, item):
        if self.tos == self.maxstk-1:
            print("Overflow!")
            return

        else:
            self.stack.append(item)
            self.tos += 1
            return self.stack

    def top(self):
        if self.tos == -1:
            print("Underflow!")
            return

        return self.stack[self.tos]

    def isEmpty(self):
        return self.tos == -1

    def display(self):
        if self.tos == -1:
            print("Empty Stack")
        else:
            print("Stack:")
            maximum = len(str(max(self.stack)))
            for i in range(len(self.stack)-1, -1, -1):
                print("|", " "*maximum, self.stack[i], " "*maximum, "|")
            print()
