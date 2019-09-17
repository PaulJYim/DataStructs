class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Bst:
    def __init__(self):
        self.root = None
        self.depth = 0
        self.height = 0

    def add_node(self, val):
        if(self.root is None):
            node = Node(val)
            self.root = node
        else:
            temp = self.root
            found = False

            while(found):
                if(val < temp.val and temp.left is not None):
                    node = Node(val)
                    temp.left = node
                    found = True
                elif(val > temp.val and temp.right is not None):
                    node = Node(val)
                    temp.right = node
                    found = True
                elif(val < temp.val and temp.left is None):
                    temp = temp.left
                else:
                    temp = temp.right
                    
    def search(self, val):
        if (self.root is None):
            print("Tree is empty")
        else:
            cursor = self.root

            while(cursor is not None):
                if(val == cursor.val):
                    return cursor

                elif(val < cursor.val):
                    cursor = cursor.left
                else:
                    cursor = cursor.right
