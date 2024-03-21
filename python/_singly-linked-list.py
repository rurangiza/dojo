from typing import List

class Node:
    def __init__(self, value=-1):
        self.value = value;
        self.next = None

class LinkedList:
    
    # LinkedList() will initialize an empty linked list
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.size = 0
    
    # int get(int i) will return the value of the ith node (0-indexed).
    # If the index is out of bounds, return -1
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr, count = self.head.next, 0
        while curr and count < index:
            count += 1
            curr = curr.next
        if curr:
            return curr.value        

    # void insertHead(int val) will insert a node with val at the head of
    # the list
    def insertHead(self, val: int) -> None:
        newnode = Node(val)
        newnode.next = self.head.next
        self.head.next = newnode
        if self.size == 0:
            self.tail.next = newnode
        self.size += 1

    # void insertTail(int val) will insert a node with val at the tail
    # of the list
    def insertTail(self, val: int) -> None:
        newnode = Node(val)
        lastnode = self.tail.next

        if lastnode:
            lastnode.next = newnode
            self.tail.next = newnode
        else:
            self.tail.next = newnode
            self.head.next = newnode
        self.size += 1

    # int remove(int i) will remove the ith node (0-indexed). If the index
    # is out of bounds, return false, otherwise return true
    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        
        curr, count = self.head, 0
        while curr.next and count < index:
            count += 1
            curr = curr.next
        
        if curr.next:
            skip = curr.next
            target = skip.next
            curr.next = target
            if target == None:
                self.tail.next = curr
            self.size -= 1

        return True

    # int[] getValues() return an array of all the values in the linked list,
    # ordered from head to tail
    def getValues(self) -> List[int]:
        arr = []
        curr = self.head.next
        while curr:
            arr.append(curr.value)
            curr = curr.next
        return arr

def main():
    pass

if __name__ == '__main__':
    main()
