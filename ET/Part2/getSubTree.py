import xml.etree.ElementTree as ET

from Part2.preorder import preorder

def getSubTree(treeA):
    # return inner subtrees (each as a list) in an array of *tree lists*
    # treeA is our parameter
    # trees[] contains the full subtrees lists (represented by node Element, each element can have its children accessed also)
    
    trees = []
    treeA_root = treeA.getroot()

    # Looping through all nodes of treeA
    for child in treeA_root:
        trees.append(child)

    #trees = preorder(treeA_root)
    #print(trees)
    return trees






    #DEMO TO TRY IT OUT IN xml2tree.py

# get first subtree A of tree 2
# A = getSubTree(tree2)
# #print(A[0])
# for child in A[1]:
#     print(child)
    
