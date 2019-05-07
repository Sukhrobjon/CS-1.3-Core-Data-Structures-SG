#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.list.size == 0

    def length(self):
        """Return the number of items in this stack."""
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) prepend uses the .head property 
        to add new node"""
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty.
        Running time: O(1) accessing head data is constant time"""
        
        if self.is_empty(): 
            return None # stack is empty
            
        # return the head node (top item) in the stack 
        return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) again accessing head node is constant time
        and we always pop from the head node."""
    
        if(self.is_empty()):
            raise ValueError("Stack is empty.")
        
        # get top node head
        top_item = self.peek() 
        
        self.list.delete(top_item)

        return top_item
        

# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: [average] O(1) appending item at the of dynamic
        array is constant time."""
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty.
        Runnning time: O(1) because to peek we need to access item at 
        last index"""
        
        if self.is_empty():
            return None
        
        return self.list[-1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) deleting last item from the dynamic array 
        is also constant time operation"""
        
        if self.is_empty():
            raise ValueError("Stack is empty.")
        
        # when no parameter passed in pop() it pops the last element 
        # in the list so we dont need to specify the index here
        return self.list.pop()


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack

# print("Stack")
