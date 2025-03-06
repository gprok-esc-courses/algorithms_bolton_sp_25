
class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        value = self.top()
        if value is not None:
            self.data.pop(-1)
        return value

    def top(self):
        if self.is_empty():
            return None 
        else: 
            return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0
    

stack = Stack()

stack.push(11)
stack.push(15)
stack.push(34)

print(stack.top())  # 34
print(stack.pop())  # 34
print(stack.top())  # 15
stack.pop()
stack.pop()
print(stack.top())  # None
