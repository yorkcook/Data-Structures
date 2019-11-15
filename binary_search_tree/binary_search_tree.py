import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
         

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value:
            if self.right and self.right.contains(target):
                return True       
        elif target < self.value:
            if self.left and self.left.contains(target):
                return True
        else:
            return False 

    # Return the maximum value found in the tree
    def get_max(self):
        while self.right:
            self = self.right
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left and self.right:
            self.left.for_each(cb)
            self.right.for_each(cb)
        elif self.left:
            self.left.for_each(cb)
        elif self.right:
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # make stack
        stack = []
        # put the root in the stack
        stack.append(node)

        # while stack is not empty
        while (len(stack) > 0):
            # Pop the top item in the stack
            node = stack.pop(0)
            print(node.value)
        # look right    
        if node.right:
            #push right to the stack
            stack.append(node.right)
        # look left    
        if node.left:
            # if there is a left, push to stack
            stack.append(node.left)

    













    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # make queue
        queue = []
        # push root into queue
        queue.append(node)

        # while queue not empty
        while (len(queue) > 0):
            print(queue[0].value)
            node = queue.pop(0)
            #if left 
            if node.left:
                #add left to back
                queue.append(node.left)
            #if right
            if node.right:
                #add right to back
                queue.append(node.right)


   

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
