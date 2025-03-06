

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        value = self.next()
        if value is not None:
            self.data.pop(0)
        return value

    def next(self):
        if self.is_empty():
            return None 
        else: 
            return self.data[0]

    def is_empty(self):
        return len(self.data) == 0
    

stack = Queue()

stack.enqueue(11)
stack.enqueue(15)
stack.enqueue(34)

print(stack.next())     # 11
print(stack.dequeue())  # 11
print(stack.next())     # 15
stack.dequeue()
stack.dequeue()
print(stack.next())  # None