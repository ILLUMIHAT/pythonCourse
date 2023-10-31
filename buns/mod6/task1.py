class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def push(self, val):
        newNode = Node(val)
        if self.start is None:
            self.start = newNode
            return
        curr = self.start
        while curr.next:
            curr = curr.next
        curr.next = newNode

    def get(self, index):
        curr = self.start
        k = 0
        while curr and k < index - 1:
            curr = curr.next
            k += 1
        return curr.data

    def remove(self, index):
        if index < 0:
            return
        if index == 0:
            self.start = self.start.next
            return
        curr = self.start
        k = 0
        while curr and k < index - 1:
            curr = curr.next
            k += 1
        if curr and curr.next:
            curr.next = curr.next.next

    def insert(self, n, val):
        if n < 0:
            return
        newNode = Node(val)
        if n == 0:
            newNode.next = self.start
            self.start = newNode
        else:
            curr = self.start
            k = 0
            while curr and k < n - 1:
                curr = curr.next
                k += 1
            if curr:
                newNode.next = curr.next
                curr.next = newNode

    def __iter__(self):
        return IteratorLinkedList(self.start)

class IteratorLinkedList:
    def __init__(self, start):
        self.curr = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr is None:
            raise StopIteration
        else:
            data = self.curr.data
            self.curr = self.curr.next
            return data
