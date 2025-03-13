
class MaxHeap:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)
        self.heapify_up()

    def get(self):
        if self.is_empty():
            return None 
        maximum = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop(-1)
        self.heapify_down() 
        return maximum

    def is_empty(self):
        return len(self.data) == 0

    def get_parent(self, pos):
        return (pos - 1) // 2
    
    def get_left_child(self, pos):
        return pos * 2 + 1
    
    def get_right_child(self, pos):
        return pos * 2 + 2

    def heapify_up(self):
        pos = len(self.data) - 1
        while pos > 0:
            parent = self.get_parent(pos)
            if self.data[pos] > self.data[parent]:
                self.data[pos], self.data[parent] = self.data[parent], self.data[pos] 
                pos = parent
            else:
                break

    def in_heap_list(self, pos):
        return pos < len(self.data)

    def get_max_child(self, pos):
        left = self.get_left_child(pos)
        right = self.get_right_child(pos)
        if self.in_heap_list(left) and self.in_heap_list(right):
            if self.data[left] > self.data[right]:
                return left
            else:
                return right
        elif  self.in_heap_list(left):
            return left 
        else:
            return None

    def heapify_down(self):
        pos = 0
        max_child = self.get_max_child(pos) 
        while max_child is not None:
            if self.data[pos] < self.data[max_child]:
                self.data[pos], self.data[max_child] = self.data[max_child], self.data[pos]
                pos = max_child
                max_child = self.get_max_child(pos)
            else:
                break
            

if __name__ == '__main__':
    heap = MaxHeap()
    m = heap.get()
    print("MAX", m)

    heap.add(1)
    heap.add(5)
    heap.add(36)
    heap.add(67)
    heap.add(20)
    heap.add(90)
    heap.add(7)
    heap.add(87)
    heap.add(109)
    heap.add(2)
    heap.add(77)
    print(heap.data)
    m = heap.get()
    print("MAX", m)
    print(heap.data)
    m = heap.get()
    print("MAX", m)
    print(heap.data)
    m = heap.get()
    print("MAX", m)
    print(heap.data)