class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Deque:
    def __init__(self):
        self.left = None  # Points to the first node
        self.right = None  # Points to the last node

    def isEmpty(self) -> bool:
        return self.left is None

    def append(self, value: int) -> None:
        newNode = ListNode(value)
        if self.isEmpty():
            # If the deque is empty, both left and right point to the new node
            self.left = self.right = newNode
        else:
            # Add the new node to the end and update `self.right`
            self.right.next = newNode
            self.right = newNode

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value)
        if self.isEmpty():
            # If the deque is empty, both left and right point to the new node
            self.left = self.right = newNode
        else:
            # Add the new node to the front and update `self.left`
            newNode.next = self.left
            self.left = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        if self.left == self.right:
            # If there's only one element, clear the deque
            val = self.right.val
            self.left = self.right = None
            return val
        # Traverse to the second-to-last node
        curr = self.left
        while curr.next != self.right:
            curr = curr.next
        # Update `self.right` and return the value
        val = self.right.val
        curr.next = None
        self.right = curr
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        val = self.left.val
        self.left = self.left.next
        if not self.left:
            # If the deque becomes empty, reset `self.right`
            self.right = None
        return val


