class BST:
    class _node_:
        def __init__(self, ele):
            self.left = None
            self.right = None
            self.data = ele

    def __init__(self):
        self.root = None
        self.count = 0

    def is_empty(self):
        return self.count == 0  # Should check if count is 0, not None
    
    def get_count(self):
        return self.count
    
    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)  # Right subtree first
            print('    ' * level + str(node.data))  # Print current node
            self.print_tree(node.left, level + 1)   # Left subtree next

    def add_node(self, ele):
        new_node = self._node_(ele)
        if self.is_empty():  # Tree is empty, create root
            self.root = new_node
        else:
            curNode = self.root
            while curNode is not None:
                if ele < curNode.data:
                    if curNode.left is None:  # If left child is None, add node
                        curNode.left = new_node
                        break
                    else:
                        curNode = curNode.left
                elif ele > curNode.data:
                    if curNode.right is None:  # If right child is None, add node
                        curNode.right = new_node
                        break
                    else:
                        curNode = curNode.right
                else:
                    # If the element is already in the tree, do nothing
                    break

        self.count += 1  # Increment the count after adding a new node
        