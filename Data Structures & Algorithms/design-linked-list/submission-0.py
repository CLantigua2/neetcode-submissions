class LinkedList:
    def __init__(self, value):
        self.prev = None
        self.val = value
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = LinkedList(-1)
        self.tail = LinkedList(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        current = self.head.next
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = LinkedList(val)
        first = self.head.next
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first
        first.prev = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_tail = LinkedList(val)
        last = self.tail.prev
        self.tail.prev = new_tail
        new_tail.next = self.tail
        new_tail.prev = last
        last.next = new_tail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        # Find node before target
        prev = self.head
        for _ in range(index):
            prev = prev.next
        # prev now points to node before insertion point
        new_node = LinkedList(val)
        next_node = prev.next
        prev.next = new_node
        new_node.prev = prev
        new_node.next = next_node
        next_node.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        # Find node before target
        prev = self.head
        for _ in range(index):
            prev = prev.next
        # prev now points to node before deletion
        target = prev.next
        next = target.next
        prev.next = next
        next.prev = prev
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
