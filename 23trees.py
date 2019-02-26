
class Node(object):
    def __init__(self, data=[]):
        # items that need to be stored
        self.data = data
        self.left, self.right, self.middle = None, None, None
        self.parent = None
        
    def is_leaf(self):
        if (self.left == None and self.right == None and self.middle == None):
            return True
        assert (self.left == None and self.right == None) or (self.left != None and self.right != None), "Invalid Node Found"
        return False

    def is_branch(self):
        if (self.is_leaf()) : 
            return False
        elif (len(self.data) == 1):
            assert (self.middle == None), "Invalid Node Found"
            assert (self.left != None and self.right != None), "Invalid Node Found"
        elif (len(self.data) == 2):
            assert self.left != None and self.right != None and self.middle != None, "Invalid Node Found"
        return True

    def insert(self, item):
        if (len(self.data) > 2):
            raise ValueError("Too Many Values in Node. Cannot Insert.")
        self.data.append(item)
        self.data.sort() # fast because 3 elements or less in list
        return


class Tree23(object):
    def __init__(self, items=[]):
        self.root = None
        for item in items:
            self.add(item)

        self.length = 0
        self.depth = 0
    
    #### helper functions ####

    # get direction for tree traversal when finding a valid node for adding item
    def getDirection(self, item, node):
        assert node.is_branch(), "Cannot get direction for leaf node"
        # deals with lead case in findValidNode
        if (len(node.data) == 1):
            if (item < node.data[0]):
                return 'left'
            elif (item > node.data[0]):
                return 'right'
            elif (item == node.data[0]):
                raise ValueError("Duplicated not allowed ----YET----")
        elif (len(node.data == 2)):
            if (item < node.data[0]):
                return 'left'
            elif (item > node.data[1]):
                return 'right'
            elif (node.data[0] < item < node.data[1]):
                return 'middle'
            elif (item == node.data[0] or item == node.data[1]):
                raise ValueError("Duplicated not allowed ----YET----")
        
        # else: length of data is 0 or more than 2
        raise ValueError("Invalid Node")

    # tree traversal: finds the root node for which the item could belong on left, right, or middle
    # bottom-most node where the item could be added to
    def findValidNode(self, item, node):
        assert node is not None, "Given node with None value"

        if (node.is_leaf()): # no left/right subtrees
            return node
        
        # else
        direction = self.getDirection(item, node)
        if (direction == "left"):
            return self.findValidNode(item, node.left)
        elif (direction == "right"):
            return self.findValidNode(item, node.right)
        elif (direction == "middle"):
            return self.findValidNode(item, node.middle)
        
        assert node.is_leaf(), "Invalid node, its not a leaf."
        return node

    def balance(self, node):
        if (len(node.data) < 3):
            return
        assert  node.is_leaf(), "Why are you balancing a branch???"
        # 3 elements in node
        min_elem = node.data.pop(0)
        left = Node([min_elem])
        max_elem = node.data.pop()
        right = Node([max_elem])
        assert len(node.data) == 1, "Data pops didn't work??"
        left.prev = node
        right.prev = node
        # update node by adding children
        node.left = left
        node.right = right
        assert node.is_branch(), "Balanced, but not a branch???"
        # self.depth += 1
        return

    #### implementation functions ####

    # adds item to the tree and self balances
    def add(self, item):
        if (self.root is None): # empty tree, needs to be initialized
            self.root = Node([item])
            return
        
        # else: find valid node to insert
        node = self.findValidNode(item, self.root)
        assert node.is_leaf(), "Invalid Node for adding item"
        node.insert(item)
        # balance if needed
        self.balance(node)
        # self.length += 1
        return

    def printTreeHelper(self, node):
        if (node == None):
            return

        self.printTreeHelper(node.left)
        print(node.data[0])
        if (len(node.data) == 2):
            self.printTreeHelper(node.middle)
            print(node.data[1])
        self.printTreeHelper(node.right)
        return


    def printTree(self):
        return self.printTreeHelper(self.root)

    def printDepthTreeHelper(self, node, depth):
        if (node == None):
            return
        print (depth + node.data)
        self.printDepthTreeHelper(node.left, depth[:-1])
        self.printDepthTreeHelper(node.right, depth[:-1])

    def printDepthTree(self):
        # depth = " "*self.depth
        self.printDepthTreeHelper(node, depth)


if __name__ == '__main__':
    items = [5,8,12,4,2,10]
    tree = Tree23(items)
    tree.printTree()
