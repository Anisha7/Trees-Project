
class Node(object):
    def __init__(self, data=[]):
        # items that need to be stored
        self.data = data
        self.left = None
        self.right = None
        self.middle = None

    def insert(self, item):
        if (len(self.data) < 3):
            self.data.append(item)
            self.data.sort()
            return True
        return False


class Tree23(object):
    def __init__(self, items=[]):
        self.head = None
        for item in items:
            self.add(item)
    
    # tree traversal
    def findInsertionLocation(self, item, node):
        if (node == None):
            return None
        
        n = len(node.data)
        
        # left
        if (n >= 1 and item < node.data[0]):
            if (node.left != None):
                return self.findInsertionLocation(item, node.left)
            return node

        # right with len = 2
        if (n == 2 and item > node.data[1]):
            if (node.right != None):
                return self.findInsertionLocation(item, node.right)
            return node
        
        # right with len = 1
        if (n == 1 and item > node.data[0]):
            if (node.right != None):
                return self.findInsertionLocation(item, node.right)
            return node

        # middle with len = 2
        if (n == 2 and item > node.data[1] and item < node.data[2]):
            if (node.middle != None):
                return self.findInsertionLocation(item, node.middle)
            return node
        
        return node


    def add(self, item):
        # adding first element
        if (self.head == None):
            self.head = Node([item])
       
        # all other cases
        # find valid empty spot: tree node at the lowest level where it fits
        temp = self.findInsertionLocation(item, self.head)
        
        # if temp is uninitialized
        if (temp == None):
            temp = Node()
        temp.insert(item)

        # balance tree
        self.balanceNode(temp)
        return

    # handle individual balancing and shifting
    def balanceNode(self, node):
        # doesn't need to be balanced
        if (len(node.data) < 3):
            return node
        
        # balance
        newHead = Node([node.data[1]])
        newLeft = Node(node.data[0])
        newRight = Node(node.data[2])
        
        newLeft.left = node.left
        newRight.left = node.middle
        newRight.right = node.right

        newHead.left = newLeft
        newHead.right = newRight

        return node

    # find nodes that need balancing and balance them
    def balanceHelper(self, node):
        if (node == None):
            return
        
        if (len(node.data) == 3):
            node = self.balanceNode(node)
        
        self.balanceHelper(node.left)
        self.balanceHelper(node.right)
        return

    # balance entire tree
    def balance(self):
        return self.balanceHelper(self.head)

    def find(self, item):
        return
    
    def remove(self, item):
        return

    def printTreeHelper(self, node):
        if (node == None):
            return

        self.printTreeHelper(node.left)
        print(node.data)
        self.printTreeHelper(node.right)
        return

    def printTree(self):
        return self.printTreeHelper(self.head)

    