
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
    def findInsertionLocation(self, item, node, prev):
        if (node == None):
            return node, prev
        
        n = len(node.data)
        
        # left
        if (n >= 1 and item < node.data[0]):
            if (node.left != None):
                return self.findInsertionLocation(item, node.left, node)
            return node, prev

        # right with len = 2
        if (n == 2 and item > node.data[1]):
            if (node.right != None):
                return self.findInsertionLocation(item, node.right, node)
            return node, prev
        
        # right with len = 1
        if (n == 1 and item > node.data[0]):
            if (node.right != None):
                return self.findInsertionLocation(item, node.right, node)
            return node, prev

        # middle with len = 2
        if (n == 2 and item > node.data[1] and item < node.data[2]):
            if (node.middle != None):
                return self.findInsertionLocation(item, node.middle, node)
            return node, prev
        
        return node, prev


    def add(self, item):
        print('in add')
        print(item)
        # adding first element
        if (self.head == None):
            self.head = Node()
       
        # all other cases
        # find valid empty spot: tree node at the lowest level where it fits
        temp, prev = self.findInsertionLocation(item, self.head, self.head)
        if (temp == None):
            temp = prev

        # if temp is uninitialized
        if (temp == None):
            temp = Node()
        temp.insert(item)
        print(temp.data)
        # balance tree
        self.balanceNode(temp, prev)
        print('end of add')
        return

    # handle individual balancing and shifting
    def balanceNode(self, node, prev):
        print('in balance node')
        # doesn't need to be balanced
        if (len(node.data) < 3):
            print('doesnt need balancing')
            return node
        
        # balance
        if (prev == None):
            newHead = Node([node.data[1]])
            newLeft = Node([node.data[0]])
            newRight = Node([node.data[2]])
            
            newLeft.left = node.left
            newRight.left = node.middle
            newRight.right = node.right

            newHead.left = newLeft
            newHead.right = newRight

            prev = newHead
            return prev
        print(newHead.left.data)
        print(newHead.data)
        print(newHead.right.data)
        # prev exists
        else:
            prev.data.insert(node.data.pop(1))
            prev.middle.insert(node.data.pop(2))
            if (len(prev.data) >= 3):
                # whats prev of prev???-
                self.balanceNode(prev)
            if (len())
        print('end of balance node')
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

if __name__ == '__main__':
    items = [5,8,12,4,2,10]
    tree = Tree23(items)
    tree.printTree()
