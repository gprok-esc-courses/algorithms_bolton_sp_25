# This is a simple hash table with values 0-9

from simply_linked_list import LinkedList

def hash_function(n):
    return n % 10

class HashTable:
    def __init__(self):
        self.table = [LinkedList() for i in range(10)]

    def add(self, value):
        hv = hash_function(value)
        self.table[hv].add(value)

    def display(self):
        index = 0
        for linked_list in self.table:
            print(index, end='. ')
            linked_list.display()
            index += 1



ht = HashTable()
ht.add(67)
ht.add(40)
ht.add(27)
ht.add(43)
ht.add(81)
ht.add(11)
ht.add(58)
ht.add(19)
ht.display()