# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # go left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        else:
            # go right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            # go left
            if not self.left:
                return False
            else:
                return self.left.contains(target)

        else:  # target is >= self.value
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        # if not self.right:
        #     return self.value
        # return self.right.get_max()

        max_value = self.value
        current = self

        while current:
            # if current is greater than max, update
            if current.value > max_value:
                max_value = current.value

            current = current.right

        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # cb(self.value)

        # if self.left:
        #     self.left.for_each(cb)
        # if self.right:
        #     self.right.for_each(cb)
        stack = []
        stack.append(self)

        while len(stack):
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     # check if current node is empty (base case)
    #     # traverse left tree
    #     if node is not None:
    #         if node.left:
    #             self.in_order_print(node.left)
    #         print(node.value)
    #         if node.right:
    #             self.in_order_print(node.right)

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal

    # def bft_print(self, node):
    #     q = Queue()
    #     q.enqueue(node)
    #     while q.len() > 0:
    #         current_pop = q.dequeue()
    #         print(current_pop.value)
    #         if current_pop.left:
    #             q.enqueue(current_pop.left)
    #         if current_pop.right:
    #             q.enqueue(current_pop.right)

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     stack = Stack()
    #     stack.push(node)
    #     while stack.len() > 0:
    #         current_pop = stack.pop()
    #         print(current_pop.value)
    #         if current_pop.left:
    #             stack.push(current_pop.left)
    #         if current_pop.right:
    #             stack.push(current_pop.right)

    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print In-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
