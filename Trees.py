
class BinaryTree:
    def __init__(self, rootObj=None):
        self.key = rootObj
        self.left = None
        self.right = None
        
	def findMin(self):
		"""Returns smallest item of all subtrees"""
		current_node = self
		while current_node.left:
			current_node = current_node.left
		return current_node.key
        
    def find(self, item):
        ''' Uses recursion to return True if item is in the tree, returns
        False if the item is not in the tree. '''
        if item == self.key:
            return True
        elif item < self.key:
            if self.left == None:
                return False
            else:
                return self.left.find(item)
        elif item > self.key:
            if self.right == None:
                return False
            else:
                return self.right.find(item)
        else:
            return False
            
    def findMax(self):
		"""Returns largest item of all subtrees"""
		current_node = self
		while current_node.right:
			current_node = current_node.right
		return current_node.key
		
    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t
            
    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t
            
    def insert(self, newNode):
        if newNode < self.key:
            if (self.left == None) or (newNode > self.left.key):
                self.insertLeft(newNode)
            else:
                self.left.insert(newNode)
                
        else:
            if (self.right == None) or (newNode < self.right.key):
                self.insertRight(newNode)
            else:
                self.right.insert(newNode)

    def getRootVal(self):
        return self.key
    
    def setRootVal(self, value):
        self.key = value
        
    def getLeftChild(self):
        return self.left
    
    def getRightChild(self):
        return self.right
    
    def getItemCount(self):
        if self.left:
            self.left.getItemCount()
        incrementItemCount()
        if self.right:
            self.right.getItemCount()
    
    def traversePreorder(self):
        '''Preorder traversal of the tree. Prints the root first, then
        the branches from left to right'''
        print self.key
        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()
            
    def traversePostorder(self):
        '''Postorder traversal of tree. Prints braches from left to right,
        then prints the root'''
        if self.left:
            self.left.traversePostorder()
        if self.right:
            self.right.traversePostorder()
        print self.key
        
    def traverseInorder(self):
        '''Inorder traversal of tree. Prints left branch, then root, then
        the right branch'''
        if self.left:
            self.left.traverseInorder()
        print self.key
        if self.right:
            self.right.traverseInorder()

itemcount = 0

def getItemCount(tree):
    global itemcount
    itemcount = -1 #reset itemcount each time
    
    tree.getItemCount()
    return itemcount
    
def incrementItemCount():
    global itemcount
    itemcount += 1
    
class AVLtree(BinaryTree):
    ''' Invented by Adel'son-Velskii and Landis in 1962, an AVL tree is
    a binary search tree that is always balanced. The length of the longest
    path to leaves in the left subtree and the length of the longest path
    to leaves in the right subtree differ by ONE at most. '''
    def __init__(self, rootObj):
        BinaryTree.__init__(self, rootObj)
        
class SplayTree(BinaryTree):
    ''' A splay tree is a binary search tree on which splay operations are
    defined. '''
    def __init__(self, rootObj):
        BinaryTree.__init__(self, rootObj)
        
class Btree2_3:
    ''' The B-tree was invented by Bayer and McCreight in 1972. It maintains
    balance, the paths from the root to leaves are all equal. This is a 2-3 
    B-tree which means it has 2 or 3 children and maintain 2 or 3 keys. '''
    def __init__(self, rootKey1, rootKey2, rootKey3=None):
        self.key1 = rootKey1
        self.key2 = rootKey2
        self.key3 = rootKey3
        self.child1 = None
        self.child2 = None
        self.child3 = None
        
    def find(self, item):
        if item < self.key2:
            if self.child1 == None:
                if item == self.key1:
                    return True
                return False
            else:
                return self.child1.find(item)
        elif self.key2 <= item < self.key3:
            if self.child2 == None:
                if item == self.key2:
                    return True
                return False
            else:
                return self.child2.find(item)
        elif item >= self.key3:
            if self.child3 == None:
                if item == self.key3:
                    return True
                return False
            else:
                return self.child3.find(item)
            
    def insert(self, item):
        ''' NOT COMPLETE '''
        if item < self.key2:
            if self.child1 == None:
                if item < self.key1:
                    pass
                    #insert to left
                elif item > self.key1:
                    pass
                    #insert to right
            else:
                return self.child1.find(item)
        elif self.key2 <= item < self.key3:
            if self.child2 == None:
                if item < self.key2:
                    pass
                    #insert to left
                elif item > self.key2:
                    pass
                    #insert to right
            else:
                return self.child2.find(item)
        elif item >= self.key3:
            if self.child3 == None:
                if item < self.key3:
                    x = Btree2_3(None, item)
                    self.child3 = x
                    #insert to left
                elif item > self.key3:
                    x = Btree2_3(None, item)
                    
                    #insert to right
            else:
                self.child3.find(item)
