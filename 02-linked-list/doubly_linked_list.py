
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None 


class DoublyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def add(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def display(self):
        iter = self.head 
        while iter is not None:
            print(iter.data)
            iter = iter.next

    def remove(self, value):
        iter = self.head
        while iter is not None:
            if iter.data == value:
                if iter == self.head and iter == self.tail:
                    # It's the only element in the list
                    self.head = self.tail = None 
                elif iter == self.head: 
                    # We delete the first element
                    self.head = self.head.next
                    self.head.prev = None 
                elif iter == self.tail:
                    # We delete the last element 
                    self.tail = self.tail.prev 
                    self.tail.next = None
                else:
                    # We delete some element in the middle
                    iter.prev.next = iter.next 
                    iter.next.prev = iter.prev 
                return True 
            iter = iter.next 
        return False


list = DoublyLinkedList()
list.add(45)
list.add(36)
list.add(11)
list.add(15)
list.add(33)
list.add(78)
list.display()
print("DEL 15")
list.remove(15)
list.display()
print("DEL FIRST 78")
list.remove(78)
list.display()
print("DEL LAST 45")
list.remove(45)
list.display()
print("DELETE ALL")
list.remove(33)
list.remove(36)
list.remove(11)
list.display()
print("ADD SOMETHING")
list.add(100)
list.display()
