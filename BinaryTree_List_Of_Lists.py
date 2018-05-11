
def BinaryTree(rootName):
    '''List of lists binary tree'''
    return [rootName, [], []]

def insertLeft(root, newBranchName):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranchName, t, []])  # make the original branch a branch of the new node
    else:
        root.insert(1, [newBranchName, [], []])
    return root

def insertRight(root, newBranchName):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranchName, [], t])  # make the original branch a branch of the new node
    else:
        root.insert(2, [newBranchName, [], []])
    return root