class Stack:
    def __init__(self):
        self.stack = []
        self.sizeStack = 0

    def push(self, element):
        self.stack.append(element)
        self.sizeStack += 1

    def pop(self):
        if not self.empty():
            self.stack.pop(self.sizeStack - 1)
            self.sizeStack -= 1
        else:
            print('Stack is empty!')

    def top(self):
        if not self.empty():
            return self.stack[-1]
        return None

    def empty(self):
        if self.sizeStack == 0:
            return True
        return False

    def print(self):
        print('Stack:' + str(self.stack))

    def printSize(self):
        print('Size:[' + str(self.sizeStack) + ']')


stack = Stack()
stack.print()
stack.pop()

stack.push(1)
stack.print()
print('Top element:[' + str(stack.top()) + ']')

stack.push(2)
stack.push(3)
stack.push(4)
stack.print()
print('Top element:[' + str(stack.top()) + ']')

stack.printSize()

stack.pop()
stack.print()
stack.printSize()
