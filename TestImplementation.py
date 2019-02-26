
class Node(object):
    def __init__(self, data=[]):
        # items that need to be stored
        self.data = data
        self.left = None
        self.right = None
        self.middle = None  # ONLY USED WITH 3 NODE, ELSE NONE
        self.parent = None

    def is_leaf(self):
        # check len(data) and .left/.right (.middle for 3-node)

    def is_branch(self):
        # check that both children exist (2 node) or all 3 children exist (3-node), else raise Error


    def insert(self, item):
        if (len(self.data) < 3):
            self.data.append(item)
            self.data.sort()
            return
        raise ValueError("Node has too many elements. Cannot insert.")


class Tree23(object):
    def __init__(self, items=[]):
        self.root = None
        for item in items:
            self.add(item)
    
    # find if item belongs in left, right, or middle
    def direction(self, item, node):
        # if (node == None):
        #     return None
        # if (node.data[0] > item):
        #     return 'left'
        # if (len(node.data) == 2 and node.data[1] < item):
        #     return 'right'
        # if (len(node.data) == 1 and node.data[0] < item):
        #     return 'right'
        # if (len(node.data) == 1 and node.data[0] < item and node.data[1] > item):
        #     return 'middle'
        # return 'curr'

        if node is None:
            return None
        assert 1 <= len(node.data) <= 2
        # Check if node is a leaf or branch

        # If node is a branch ...
        if len(node.data) == 1:  # 2-node
            if item < node.data[0]:
                if node.left is None:
                    return 'curr'
                return 'left'
            elif item > node.data[0]:
                return 'right'  # FIXME: Case 2. (add 8 to a single node with 5 in it)
            elif item == node.data[0]:
                raise ValueError("Equal values not supported (yet)")
        elif len(node.data) == 2:  # 3-node
            if item < node.data[0]:
                return 'left'
            elif item > node.data[1]:
                return 'right'
            elif node.data[0] < item < node.data[1]:
                return 'middle'
            elif item == node.data[0] or item == node.data[1]:
                raise ValueError("Equal values not supported (yet)")


    # tree traversal: finds the root node for which the item could belong on left, right, or middle
    # bottom-most node where the item could be added to
    def findInsertionLocation(self, item, node):
        direction = self.direction(item, node)
        assert node is not None, "error msg"
        if (node == None):
            raise ValueError("Give node with None value")
            # return None, direction
        
        solution, direc = node, 'curr'
        if (direction == 'left'):
            if (node.left == None):
                return node, 'left'
            solution, direc = self.findInsertionLocation(item, node.left)
        elif (direction == 'right'):
            if (node.right == None):
                return node, 'right'
            solution, direc = self.findInsertionLocation(item, node.right)
        elif (direction == 'middle'):
            if (node.middle == None):
                return node, 'middle'
            # solution, direc = self.findInsertionLocation(item, node.middle)
            return self.findInsertionLocation(item, node.middle)
        else:
            # ???   
        # # if solution not found
        # if (solution == None):
        #     return node, 'curr'
        
        return solution, direc

    def add(self, item):
        # if empty tree, initialize
        if (self.root == None):
            self.root = Node([item])
        
        else:
            # assuming this function works
            node, direction = self.findInsertionLocation(item, self.root)
            appended = 'curr'
            
            # if leaf: append to node

            # use direction to append to proper node
            if (direction == 'left'):
                if (node.left != None):
                    # append to left
                    node.left.insert(item)
                    appended = direction
                else:
                    # append to node
                    node.insert(item)

            elif (direction == 'right'):
                if (node.right != None):
                    # append to right
                    node.right.insert(item)
                    appended = direction
                else:
                    # append to node
                    node.insert(item)

            elif (direction == 'middle'):
                if (node.middle != None):
                    # append to middle
                    node.middle.insert(item)
                    appended = direction
                else:
                    # append to node
                    node.insert(item)
            else:
                # append to node
                node.insert(item)

            # balancing if needed
            # new nodes are created only when balancing, so make sure to set the parent property then
            if (appended == 'curr' and len(node.data) >= 3):
                print('balancing: %s'%(str(node.data)))
                # balance node
                self.balanceNode(node)
            elif (appended == 'left' and len(node.left.data) >= 3):
                print('balancing: %s'%(str(node.left.data)))
                # balance left node
                self.balanceNode(node.left)
            elif (appended == 'right' and len(node.right.data) >= 3):
                print('balancing: %s'%(str(node.right.data)))
                # balance right node
                self.balanceNode(node.right)
            elif (appended == 'middle' and len(node.middle.data) >= 3):
                print('balancing: %s'%(str(node.middle.data)))
                # balance middle node
                self.balanceNode(node.middle)


    # handle individual balancing and shifting
    def balanceNode(self, node):
        assert len(node.data) == 3, "Tried to balance a non-full node"
        rightItem = node.data.pop()
        print(rightItem)
        middleItem = node.data.pop()
        print(middleItem)

        # if we are on root node, parent will be none
        # so we create a new root node
        if (node.parent == None):
            new_parent = Node()
            node.parent = new_parent
            self.root = node.parent

        # NOTE: There should only be a middle node if there are 2 data items
        # Else, handle differently.
        
        # push (promote) middle item into parent
        node.parent.insert(middleItem)
        # node.data.pop()
        print(node.data)
        print('parent')
        print(node.parent.data)

        # push right item into middle
        if (node.middle == None):
            # initialize middle
            new_node = Node()
            new_node.parent = node
            node.middle = new_node
        node.middle.insert(rightItem)

        # if (len(node.parent.data) >= 3):
        #     return self.balanceNode(node.parent)
        return


    def find(self, item):
        return
    

    def remove(self, item):
        return


    def printTreeHelper(self, node):
        if (node == None):
            return

        self.printTreeHelper(node.left)
        if (node.middle != None):
            print(node.data[0], end=' ')
            self.printTreeHelper(node.middle)
            print(node.data[1])
        else:
            print(node.data)
        self.printTreeHelper(node.right)
        return


    def printTree(self):
        return self.printTreeHelper(self.root)

if __name__ == '__main__':
    items = [5,8,12,4,2,10]
    tree = Tree23(items)
    tree.printTree()


# rough
    # handle individual balancing and shifting
    # TODO: CHECK AND FIX SELF.ROOT UPDATES AND NODE's OLD PARENT UPDATES
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
            # self.root = node.parent
        
        # node does have a parent
        elif (parent is not None):
            # if direction is right, not left
            # data at index 1 because middle node is removed
            if (node.parent.data[0] < node.data[1]):
                direction = 'right'

            # balancing a right node
            if direction == 'right':
                # variables
                newVal = node.data.pop(0)
                newNode = node.left
                node.left = None

                # changes
                node.parent.insert(middleVal)
                if (node.parent.middle is None):
                    node.parent.middle = Node()
                node.parent.middle.insert(newVal)
                node.parent.middle.right = newNode
                node.parent.middle.right.parent = parent.middle
                node.parent.middle.parent = parent

            # balancing a left node
            elif direction == 'left':
                # variables
                newVal = node.data.pop()
                newNode = node.right
                node.right = None

                # changes
                node.parent.insert(middleVal)
                if (node.parent.middle is None):
                    node.parent.middle = Node()
                node.parent.middle.insert(newVal)
                node.parent.middle.left = newNode
                if (newNode is not None):
                    node.parent.middle.left.parent = parent.middle
                node.parent.middle.parent = parent

        # middle node exists
        if (middleNode is not None):
            mLeft, mRight = self.splitMiddle(middleNode)
            if (direction == 'left'):
                node.right = mLeft
                # this parent refers to old parent on first check
                if (parent is not None):
                    node.parent.middle.left = mRight
                else:
                    node.parent.right.left = mRight

            elif (direction == 'right'):
                node.left = mRight
                node.parent.middle.right = mLeft
        
        print(node)
        print(node.data)
        print(node.parent)
        print(node.parent.data)
        return

            # TODO: splits the middle node
    def splitMiddle(self, node):
    # def splitMiddle(self, l1, l2):
        left = Node(node.data[0])
        right = Node(node.data[1])

        # if it has children
        if (node.is_branch()):
            left.right = node.left
            right.left = node.right
            # if middle exists: call split middle recursively
            if (node.middle != None):
                l,r = self.splitMiddle(node.middle)
                left.right.right = l
                right.left.left = r
        
        return left, right