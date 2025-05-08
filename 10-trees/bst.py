class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 
        self.parent = None 

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self):
        self.root = None 

    def is_empty(self):
        return self.root is None
    
    def find(self, value):
        iter = self.root 
        while True:
            if iter is None: 
                return None 
            elif value == iter.value:
                return iter 
            elif value > iter.value:
                iter = iter.right
            else:
                iter = iter.left
                
    def is_leaf(self, node):
        return node.left is None and node.right is None
    
    def has_one_child_only(self, node):
        return (node.left is None and node.right is not None) or (node.left is not None and node.right is None)
    
    def is_left_child(self, node):
        return node.value < node.parent.value
    
    def is_right_child(self, node):
        return node.value > node.parent.value
    
    def get_successor(self, node):
        iter = node.right
        while True:
            if iter.left is None:
                return iter 
            else: 
                iter = iter.left
    
    def remove(self, value):
        node = self.find(value) 
        if node is None:
            return False
        else: 
            # Case 1: Leaf
            if self.is_leaf(node):
                if node == self.root:
                    self.root = None 
                elif self.is_left_child(node):
                    node.parent.left = None 
                elif self.is_right_child(node):
                    node.parent.right = None
            # Case 2: One child
            elif self.has_one_child_only(node):
                child = node.left if node.left is not None else node.right 
                if node == self.root:
                    self.root = child
                elif self.is_left_child(node):
                    node.parent.left = child
                elif self.is_right_child(node):
                    node.parent.right = child
            # Case 3: Two children 
            else: 
                successor = self.get_successor(node)
                new_value = successor.value
                self.remove(successor.value)
                node.value = new_value

        
    
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node)
            self.inorder(node.right)

    def add(self, value):
        new_node = TreeNode(value)
        if self.is_empty():
            self.root = new_node
        else:
            iter = self.root
            while True:
                if value > iter.value:
                    # go right
                    if iter.right == None:
                        iter.right = new_node
                        new_node.parent = iter  
                        return 
                    else: 
                        iter = iter.right
                else: 
                    # go left
                    if iter.left == None:
                        iter.left = new_node
                        new_node.parent = iter 
                        return 
                    else:
                        iter = iter.left 

                
if __name__ == '__main__':
    tree =  BST()
    tree.add(100)
    tree.add(70)
    tree.add(180)
    tree.add(50)
    tree.add(90)
    tree.add(60)
    tree.add(160)
    tree.add(220)
    tree.add(110)
    tree.add(200)
    tree.add(250)
    tree.inorder(tree.root)

    print("Test Find")
    print(tree.find(220))
    print(tree.find(260))

    # print("Test Remove Leafs")
    # tree.remove(110)
    # tree.remove(60)
    # tree.inorder(tree.root)

    # print("Test Remove Single Childe Nodes")
    # tree.remove(50)
    # tree.remove(160)
    # tree.inorder(tree.root)

    # print("Find Successor")
    # node = tree.find(180)
    # print(tree.get_successor(node))

    print("Test Remove Two Children Nodes")
    tree.remove(100)
    # tree.remove(160)
    tree.inorder(tree.root)
        