
import random
import trees

raw_input("Press enter to start simulation...")

loops = 1000
range_low = 1
range_high = 1000

print "creating tree with " + str(loops) + " items..."
tree = trees.BinaryTree( random.randint(range_low, range_high) )

x = 0
while x < loops:
    tree.insert( random.randint(range_low, range_high) )
    x += 1
    
raw_input("tree created. press enter to print contents inorder...")
tree.traverseInorder()
print "Items in tree: " + str( trees.getItemCount(tree) )
raw_input()