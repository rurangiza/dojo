# Date: 06/11/2023

""""
Design your implementation of the linked list.
You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next.
val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need
one more attribute prev to indicate the previous node in the linked list.
Assume all nodes in the linked list are 0-indexed.
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node, prev, next = Node(val), self.left, self.left.next
        next.prev = node
        node.next = next
        node.prev = prev
        prev.next = node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        node, prev, next = Node(val), self.right.prev, self.right
        next.prev = node
        node.next = next
        node.prev = prev
        prev.next = node

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0:
            node, prev, next = Node(val), curr.prev, curr
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and curr != self.right and index == 0:
            prev, nxt = curr.prev, curr.next
            if nxt:
                nxt.prev = prev
            if prev:
                prev.next = nxt

#############################################

def main():
    obj = MyLinkedList()
    param_1 = obj.get(1)
    obj.addAtHead(10)
    obj.addAtTail(55)
    obj.addAtIndex(1,89)
    obj.deleteAtIndex(2)

if __name__ == "__main__":
    main()