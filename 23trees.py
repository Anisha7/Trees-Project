
class Node(object):
    def __init__(self, data=[]):
        # items that need to be stored
        self.data = data
        self.left, self.right, self.middle = None, None, None
        self.parent = None
        
    def is_leaf():
        if (self.left == None and self.right == None and self.middle == None):
            return True
        assert (self.left == None and self.right == None) or (self.left != None and self.right != None), "Invalid Node Found"
        return False

    def is_branch():
        if (self.is_leaf()) : 
            return False
        elif (len(data) == 1):
            assert (self.middle == None), "Invalid Node Found"
            assert (self.left != None and self.right != None), "Invalid Node Found"
        elif (len(data) == 2):
            assert self.left != None and self.right != None and self.middle != None, "Invalid Node Found"
        return True

    def insert(self, item):
        if (len(data) > 2):
            raise ValueError("Too Many Values in Node. Cannot Insert.")
        self.data.append(item)
        self.data.sort() # fast because 3 elements or less in list
        return


class Tree23(object):
    def __init__(self, items=[]):
        self.root = None
        for item in items:
            self.add(item)
    
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

    # handle individual balancing and shifting
    def balanceNode(self, node):
        if (len(node.data) < 3): # base case: its balanced
            return
        
        parent = node.parent
        middleNode = node.middle
        node.middle = None
        middleVal = node.data.pop(1)
        direction = 'left'
        # case when node doesn't have a parent (root node)
        if (parent is None):
            # new nodes
            newNode = Node([node.data.pop()]) # end value
            newParent = Node([middleVal]) # middle node that gets promoted

            # assigning values
            newNode.right = node.right
            node.right = None
            newParent.left = node
            
            # fixing pointers
            node = newParent.left
            node.parent = newParent
        
        # node does have a parent
        elif (parent is not None):
            # if direction is right, not left
            if (parent.data[1] < node.data[2]):
                direction = 'right'

            # balancing a right node
            if direction == 'right':
                # variables
                newVal = node.data.pop(0)
                newNode = node.left
                node.left = None

                # changes
                parent.insert(middleVal)
                if (parent.middle is None):
                    parent.middle = Node()
                parent.middle.insert(newVal)
                parent.middle.right = newNode
                parent.middle.right.parent = parent.middle
                parent.middle.parent = parent

            # balancing a left node
            elif direction == 'left':
                # variables
                newVal = node.data.pop()
                newNode = node.right
                node.right = None

                # changes
                parent.insert(middleVal)
                if (parent.middle is None):
                    parent.middle = Node()
                parent.middle.insert(newVal)
                parent.middle.left = newNode
                parent.middle.left.parent = parent.middle
                parent.middle.parent = parent

        # middle node exists
        if (middleNode is not None):
            mLeft, mRight = self.splitMiddle(middleNode)
            if (direction == 'left'):
                node.right = m_left
                # this parent refers to old parent on first check
                if (parent is not None):
                    node.parent.middle.left = mRight
                else:
                    node.parent.right.left = mRight

            elif (direction == 'right'):
                node.left = mRight
                node.parent.middle.right = mLeft
        
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
        self.balanceNode(node)
        return



if __name__ == '__main__':
    items = [5,8,12,4,2,10]
    tree = Tree23(items)
    tree.printTree()
