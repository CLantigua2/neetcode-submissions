class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        head = tail = Node(students[0])
        size = 1
        i = 0
        # count mismatches to check if there are no more students to pick up the last sandwich
        mismatch_count = 0

        # Place all students into LL
        for val in students[1:]:
            new_node = Node(val)
            tail.next = new_node
            tail = new_node
            size += 1

        # loop using size and the length of that index is less than sandwhiches count
        while size and len(sandwiches) > i:
            if mismatch_count == size:
                break
            elif head.val == sandwiches[i]:
                head = head.next
                if head is None:
                    tail = None
                size -= 1
                i += 1
                mismatch_count = 0
            else:
                old_head = head
                head = head.next

                if head is None:
                    head = old_head
                    tail = head
                else:
                    tail.next = old_head
                    tail = old_head
                    tail.next = None
                mismatch_count += 1

        return size
            




        