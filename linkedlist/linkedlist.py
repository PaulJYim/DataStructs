class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.length = 0

    def addnode(self,val):
        if(self.head is None):
            node = Node(val)
            self.head = node
        else:
            temp = self.head

            while(temp.next is not None):
                temp = temp.next

            node = Node(val)
            temp.next = node

        self.length += 1

    def deletelast(self):
        if(self.head is not None):
            curr = self.head
            prev = None

            while(curr.next is not None):
                prev = curr
                curr = curr.next

            if(prev is None):
                self.head = None
            else:
                prev.next = None

            self.length -= 1
        else:
            print("Empty LinkedList")

    def delete_at_value(self, val):
        if(self.head is not None):
            curr = self.head
            prev = None
            found = False
            while(curr.next is not None and not found):
                if(curr.val == val):
                    found = True
                else:
                    prev = curr
                    curr = curr.next
            if(found):
                prev.next = curr.next
                curr.next = None
            else:
                print("Node with val" ,val, "does not exist")
        else:
            print("Empty LinkedList")

    def length(self):
        return self.length


    def delete_first(self):
        if(self.head is not None):
            prev = self.head
            self.head = self.head.next
            prev.next = None
        else:
            print("Empty LinkedList")



def printLL(head):
    cursor = head

    while (cursor):
        print(cursor.val)
        cursor = cursor.next

llOne = Linkedlist()
llOne.addnode(1)
llOne.addnode(2)
llOne.addnode(3)

printLL(llOne.head)

llOne.delete_at_value(2)
printLL(llOne.head)
llOne.delete_first()
printLL(llOne.head)
