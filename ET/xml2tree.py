import xml.etree.ElementTree as ET
from CostInsTree import CostInsTree

from Nierman_Jagadish import TED
from getSubTree import getSubTree
from preorder import preorder
from sameTree import sameTree
from subTree import subTree
from nbchildren import nbchildren

import xml.dom as dom
from xml.dom.minidom import getDOMImplementation


#Part1 (not done)
#input:xml files      output: trees
tree1 = ET.parse('test1.xml') #this gets the file into a tree structure
tree2 = ET.parse('test3.xml')

tree_root1 = tree1.getroot() #this gives us the root element of the file
tree_root2 = tree2.getroot() #this gives us the root element of the file


#testing 


#METHODS

#print(nbchildren(tree2))
#print(TED(tree1=tree1, tree2=tree2))

# HOW TO ACCESS DEPTH1   THEN DEPTH 2 OF CHILDREN
# for child_d1 in tree_root1:
#      for child_d2 in child_d1:
#          print(child_d2.tag)

#How to access first Child example : test2's root has 3 children (Country x3) --> tree_root[0] / tree_root[1] / tree_root[2] 
#print(tree_root1[0])

#How to create a subtree (1st subtree of tree1=test2.xml)
# tree3 = ET.ElementTree()
# tree3._setroot(tree_root1[0])
# tree3_root = tree3.getroot()
# for child in tree3_root:
#     print(child.tag)

# PRE ORDER GETS US LIST OF SUBTREES  (a->b->c)
# print(preorder(tree_root2)) #[a]
# print(preorder(tree_root2)[0]) #<b>  (contained inside a)
# print(preorder(tree_root2)[0][0]) #<c> (contained inside b)

# get first subtree A of tree 2
# A = getSubTree(tree2)
# print(getSubTree(tree2))

# C=ET.ElementTree()
# C._setroot(A[0])
# print(getSubTree(C))

# C_root=C.getroot()
# print(C_root)
# for child in C_root:
#     print(child)


# #accessing LAST first-level-subtree
# new_tree1 = ET.ElementTree()
# for child_d1 in tree_root2: #LAST child will be set as root
#     new_tree1._setroot(child_d1)

# new_tree1_root = new_tree1.getroot()
# for child in new_tree1_root:
#     print(child)



#print(tree_root1.tag==tree_root2.tag)

#same tree is working (both via sameTree and subTree(using 2 same trees) methods) but subTree is not working (for 2 different trees)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!CHECK IF 2 (test3.xml) is SUBTREE OF 1 (test2.xml)
# print(not tree_root1)
# print(not tree_root2)


#TED(tree1, tree2)


print(subTree(tree_root1, tree_root2)) 

#print(tree_root2)
#print(preorder(tree_root2))

#print(CostInsTree(treeA=tree1, treeB=tree2))   














#treeA : tree1 
#treeB : tree2 
#tree2 not in tree1 works

#treeA : tree2 
#treeB : tree1
#tree1 not in tree2 works




#part4 (done)
#return 2 trees from the 2 xml files

#print(ET.tostring(tree_root1, encoding='utf8').decode('utf8'))
#print(ET.tostring(tree_root2, encoding='utf8').decode('utf8'))

newXML1 = ET.tostring(tree_root1, encoding='utf8').decode('utf8')
text_file1 = open("new_Test1.xml", "w")
n1 = text_file1.write(newXML1)
text_file1.close()


newXML2 = ET.tostring(tree_root2, encoding='utf8').decode('utf8')
text_file2 = open("new_Test2.xml", "w")
n2 = text_file2.write(newXML2)
text_file2.close()

