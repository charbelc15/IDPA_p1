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
from Part2_Chawathe.Chawathe import Chawathe
from Part2_Chawathe.getNodesHeights import getNodesHeights
from ES_Chawathe import backtrace
import numpy as np


#Part1 (done)
#input:xml files      output: trees
tree1 = ET.parse('xml_files/test6.xml') #this gets the file into a tree structure
tree2 = ET.parse('xml_files/test5.xml')

tree_root1 = tree1.getroot() #this gives us the root element of the file
tree_root2 = tree2.getroot() #this gives us the root element of the file

# #Part1 b) Display tree
# flagcounter = 0
# for i in tree_root1:
#     flagcounter+=1

# flag = [False]*flagcounter
# displayTree(tree_root1,flag,0,False)


#Part2 Chawathe's LD pair using same method as Display tree (cause it has depth + accesses nodes in pre order)
flagcounter1 = 0
for i in tree_root1.iter(): # .ITER() !!! TO PASS OVER ALL ELEMENTS not just children
    flagcounter1+=1

LD_pairA=[]
flag1 = [False]*flagcounter1
getNodesHeights(tree_root1,flag1,0,False,LD_pairA) #this function's job is to fill the LD_pair list which is nothing but the tag&depth of each node indexed by pre order traversal 
print(LD_pairA)

flagcounter2 = 0
for i in tree_root2.iter():
    flagcounter2+=1

LD_pairB=[]
flag2 = [False]*flagcounter2
getNodesHeights(tree_root2,flag2,0,False,LD_pairB) #this function's job is to fill the LD_pair list which is nothing but the tag&depth of each node indexed by pre order traversal 
print(LD_pairB)

#Note: chawathe returns at pos 0 : cost matrix for ES(A,B)   at pos1: ED(A,B) value (dist[M][N])
print(Chawathe(LD_pairA, LD_pairB))

cost_matrix=Chawathe(LD_pairA,LD_pairB)[0]


print(backtrace(LD_pairA, LD_pairB, cost_matrix)[0])
print(backtrace(LD_pairA, LD_pairB, cost_matrix)[1])
print(LD_pairA) #first
print(LD_pairB) #second
print(backtrace(LD_pairA, LD_pairB, cost_matrix)[2]) #new first
print(backtrace(LD_pairA, LD_pairB, cost_matrix)[3]) #new second


#nierman
#TED(tree1, tree2)













# B = getSubTree(tree2)
# treeB=ET.ElementTree()
# treeB._setroot(B[1]) 
# treeB_root = treeB.getroot()
# print(treeB_root)
# Nb_children=0
# for child in treeB_root.iter():
#         Nb_children+=1
# print(Nb_children)
# print(subTree(tree_root1,treeB_root)) # SUBTREE !!! subtree is second param
# print(CostInsTree(tree1,treeB)) # INSERT !!! tree to insert is second param
# print(CostDelTree(treeB,tree1)) # DELETE !!! tree to delete is first param
# print(sameTree(treeB_root,tree_root1))
# print(len(preorder(treeB_root)), " ", len(preorder(tree_root1)))
# print(preorder(tree_root1))

# Subtree1 = preorder(treeB_root)
# Subtree2 = preorder(tree_root1)
# list=[]
# print(Subtree1)
# print(Subtree2)
# for i in range(0, len(Subtree1)-1): #checking if order of all elements is same
#     if(Subtree1[i].tag == Subtree2[i].tag):
#             list.append("true")
# print(list)









# #to get tree Depth  # convert from root (to avoid header) to string (byte object) to get depth 
# target = MaxDepth()
# parser = XMLParser(target=target)
# xml_file = ET.tostring(tree_root1, encoding='utf8', method='xml')
# parser.feed(xml_file)
# depth = parser.close #parser.close returns the depth value

#print(preorder(tree_root1))

#trying list appending 
# list =[]
# for i in range(1,10):
#     list.append(["r.tag",i])
# print(list)

# parent = [-1, 0, 1, 6, 6, 0, 0, 2, 7]
# n = len(parent)
# height = [-1]*(n)
# res=0 
# for i in range(n):
#     res = max(res, getNodesHeights(i, parent, height))

# print(height) 
# print(res)










#testing 

#print(CostDelTree(tree2, tree1)) #deleting 1st param tree from 2nd param tree
#print(CostInsTree(tree1, tree2)) #inserting 2nd param tree in 1st param tree


#print(tree_root1.tag==tree_root2.tag)

#same tree is working (both via sameTree and subTree(using 2 same trees) methods) but subTree is not working (for 2 different trees)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!CHECK IF 2 (test3.xml) is SUBTREE OF 1 (test2.xml)
# print(not tree_root1)
# print(not tree_root2)




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

