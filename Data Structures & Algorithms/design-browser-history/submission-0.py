class Node:
    def __init__(self, val, prev=None, next=None):
        self.next = next
        self.prev = prev
        self.val = val

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)
        

    def visit(self, url: str) -> None:
        # create a new node after current and set the new nodes prev to current
        new_node = Node(url, prev=self.current)
        self.current.next = new_node
        self.current = new_node
        

    def back(self, steps: int) -> str:
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1
        return self.current.val
        

    def forward(self, steps: int) -> str:
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)