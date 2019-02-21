
class Node(object):
    def __init__(self, data=[]):
        # items that need to be stored
        self.data = data
        self.left = None
        self.right = None
        self.middle = None
        self.prev = None

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
    
    # find if item belongs in left, right, or middle
    def direction(self, item, node):
        if (node == None):
            return None
        if (node.data[0] > item):
            return 'left'
        if (len(node.data) == 2 and node.data[1] < item):
            return 'right'
        if (len(node.data) == 1 and node.data[0] < item):
            return 'right'
        if (len(node.data) == 1 and node.data[0] < item and node.data[1] > item):
            return 'middle'
        return 'curr'

    # tree traversal: finds the head node for which the item could belong on left, right, or middle
    # bottom-most node where the item could be added to
    def findInsertionLocation(self, item, node):
        direction = self.direction(item, node)
        if (node == None):
            return None, direction
        
        solution, direc = None, 'curr'
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
            solution, direc = self.findInsertionLocation(item, node.middle)
            
        # if solution not found
        if (solution == None):
            return node, 'curr'
        
        return solution, direc

    def add(self, item):
        # if empty tree, initialize
        if (self.head == None):
            self.head = Node([item])
        
        else:
            # assuming this function works
            node, direction = self.findInsertionLocation(item, self.head)
            appended = 'curr'

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
            # new nodes are created only when balancing, so make sure to set the prev property then
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
        rightItem = node.data.pop()
        print(rightItem)
        middleItem = node.data.pop()
        print(middleItem)

        # if we are on head node, prev will be none
        # so we create a new head node
        if (node.prev == None):
            node.prev = Node()
            self.head = node.prev

        # NOTE: There should only be a middle node if there are 2 data items
        # Else, handle differently.
        
        # push middle item into prev
        node.prev.insert(middleItem)
        # node.data.pop()
        print(node.data)
        print('prev')
        print(node.prev.data)

        # push right item into middle
        if (node.middle == None):
            # initialize middle
            node.middle = Node()
            node.middle.prev = node
        node.middle.insert(rightItem)

        # if (len(node.prev.data) >= 3):
        #     return self.balanceNode(node.prev)
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
            print(node.data[0])
            self.printTreeHelper(node.middle)
            print(node.data[1])
        else:
            print(node.data)
        self.printTreeHelper(node.right)
        return


    def printTree(self):
        return self.printTreeHelper(self.head)

if __name__ == '__main__':
    items = [5,8,12,4,2,10]
    tree = Tree23(items)
    tree.printTree()
