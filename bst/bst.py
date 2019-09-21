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

            while(not found):
                if(val < temp.val):
                    if(temp.left is None):
                        node = Node(val)
                        temp.left = node
                        found = True
                    temp = temp.left

                elif(val > temp.val):
                    if(temp.right is None):
                        node = Node(val)
                        temp.right = node
                        found = True
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

    def delete(self, val):
        if(self.root is None):
            print("Tree is empty")
        else:
            cursor = self.root
            prev = None
            found = False
#            if(cursor is None):
#                print("Not in tree")
#                found = True
            while(not found):

                if(val == cursor.val):
                    found = True

                elif(val < cursor.val):
                    prev = cursor
                    cursor = cursor.left

                elif(val > cursor.val):
                    prev = cursor
                    cursor = cursor.right
            if(found):
                if(cursor.right is None and cursor.left is None):
                    if(prev.val > cursor.val):
                        prev.left = None
                    elif(prev.val < cursor.val):
                        prev.right = None

                elif(cursor.right is not None):
                    temp = cursor.right
                    while(temp.left is not None):
                        temp = temp.left
                    temp.left = cursor.left
                    prev.right = cursor.right
                    cursor = None

                else:
                    prev.right = cursor.left
                    cursor.left = None



def printBST(root):

    if(root):

        printBST(root.left)
        print(root.val)
        printBST(root.right)



bstone = Bst()
bstone.add_node(10)
bstone.add_node(15)
bstone.add_node(5)
bstone.add_node(7)
bstone.add_node(4)
bstone.add_node(9)
bstone.add_node(8)
bstone.add_node(6)
bstone.delete(7)
printBST(bstone.root)

#print(bstone.search(7).val)
