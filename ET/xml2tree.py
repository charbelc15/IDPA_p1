import xml.etree.ElementTree as ET
from Part2.CostInsTree import CostInsTree
from Part2.CostDelTree import CostDelTree
from Part2.Nierman_Jagadish import TED
from Part1.displayTree import displayTree
from Part2.getSubTree import getSubTree
from Part2.preorder import preorder
from Part2.sameTree import sameTree
from Part2.subTree import subTree
from Part2.nbchildren import nbchildren

import xml.dom as dom
from xml.dom.minidom import getDOMImplementation
from xml.etree.ElementTree import XMLParser
from Part1.MaxDepth import MaxDepth


#Part1 (not done)
#input:xml files      output: trees
tree1 = ET.parse('xml_files/test4.xml') #this gets the file into a tree structure
tree2 = ET.parse('xml_files/test3.xml')

tree_root1 = tree1.getroot() #this gives us the root element of the file
tree_root2 = tree2.getroot() #this gives us the root element of the file



#to get tree Depth  # convert from root (to avoid header) to string (byte object) to get depth 
target = MaxDepth()
parser = XMLParser(target=target)
xml_file = ET.tostring(tree_root1, encoding='utf8', method='xml')
parser.feed(xml_file)
depth = parser.close #parser.close returns the depth value



#Display tree
flagcounter = 0
for i in tree_root1:
    flagcounter+=1

flag = [False]*flagcounter
displayTree(tree_root1,flag,0,False)











#testing 

#print(CostDelTree(tree2, tree1)) #deleting 1st param tree from 2nd param tree
#print(CostInsTree(tree1, tree2)) #inserting 2nd param tree in 1st param tree


#print(tree_root1.tag==tree_root2.tag)

#same tree is working (both via sameTree and subTree(using 2 same trees) methods) but subTree is not working (for 2 different trees)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!CHECK IF 2 (test3.xml) is SUBTREE OF 1 (test2.xml)
# print(not tree_root1)
# print(not tree_root2)


#TED(tree1, tree2)


#print(subTree(tree_root1, tree_root2)) 

#print(tree_root2)
#print(preorder(tree_root2))

#print(CostInsTree(treeA=tree1, treeB=tree2))   










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

