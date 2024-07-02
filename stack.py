class CustomStack:
    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.items = []

    def push(self, item):
        """
        Adds an item to the top of the stack.

        Parameters:
        item: The item to be added to the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the top item from the stack.

        Returns:
        The top item from the stack. If the stack is empty, returns None.
        """
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
        bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def peek(self):
        """
        Returns the top item from the stack without removing it.

        Returns:
        The top item from the stack. If the stack is empty, returns None.
        """
        if not self.is_empty():
            return self.items[-1]
        return None

# Test cases for CustomStack
stack = CustomStack()
print(stack.is_empty())  # Expected output: True

stack.push(10)
stack.push(20)
stack.push(30)
print(stack.peek())      # Expected output: 30

print(stack.pop())       # Expected output: 30
print(stack.pop())       # Expected output: 20
print(stack.pop())       # Expected output: 10
print(stack.pop())       # Expected output: None

print(stack.is_empty())  # Expected output: True
