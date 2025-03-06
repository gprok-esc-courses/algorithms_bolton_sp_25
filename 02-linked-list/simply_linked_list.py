
class LinkedList:
    def __init__(self):
        self.head = None 

    def add(self, value):
        new_node = ListNode(value) 
        new_node.next = self.head 
        self.head = new_node

    def display(self):
        iter = self.head 
        while iter is not None:
            print(iter.value, end=' ')
            iter = iter.next
        print()

    def contains(self, value):
        iter = self.head 
        while iter is not None:
            if iter.value == value:
                return True 
            iter = iter.next
        return False
    
    def remove(self, value):
        iter = self.head
        prev = None 
        while iter is not None:
            if iter.value == value:
                if iter == self.head:  # it's the 1st node
                    self.head = iter.next 
                else: 
                    prev.next = iter.next
                print(value, "deleted")
                return True
            prev = iter 
            iter = iter.next
        print(value, "not found")
        return False


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
    

if __name__ == "__main__":
    data = LinkedList()
    data.add(35)
    data.add(28)
    data.add(49)
    data.display()

    print(data.contains(49))
    print(data.contains(56))

    data.remove(55)
    data.remove(35)
    data.display()
    data.remove(49)
    data.display()