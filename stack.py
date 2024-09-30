from collections import deque


class Stack:
    def __init__(self, size) -> None:
        """
        Stack class to create stack with user choose
        :param size: 10
        """
        self.stack = deque(maxlen=size)
        self.size = size

    def add_element(self, data) -> None:
        """
        Takes data to add into stack and display stack data
        :param data: 10
        :return: 10 added to stack. Final stack is deque([10], maxlen=10) / Stack is Full!
        """
        if len(self.stack) == self.size:
            print("Stack is Full!")
        else:
            self.stack.append(data)
            print(f"{data} added to stack. Final stack is {self.stack}")

    def remove_element(self) -> None:
        """
        Remove element from stack(LIFO/FILO)
        :return: 10 removed from stack. Final stack is deque([], maxlen=10) / Stack is Empty!
        """
        if not self.stack:
            print("Stack is Empty!")
        else:
            print(f"{self.stack.pop()} removed from stack. Final stack is {self.stack}")

    def display(self):
        """
        Display stack data
        :return: Stack: deque([10, 20], maxlen=10)
        """
        print(f"Stack: {self.stack}")
