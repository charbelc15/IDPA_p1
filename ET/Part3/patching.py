from Part2.preorder import preorder
import xml.etree.ElementTree as ET
from Part3.delete import delete
from Part3.insert import insert
from Part3.update import update


# Charbel
# ES[i][0]  -->   [['Delete:', 7], ['Delete:', 3], ['Delete:', 2], ['Delete:', 1]]
# in the first index we have the operation "Delete:"    "Insert:"   "Update:"
# in the second index we have the position of the node (following the preorder traversal of A )

#           -->   [['Insert:', 7, 'h'], ['Insert:', 3, 'gdppc'], ['Insert:', 2, 'year'], ['Insert:', 1, 'rank']]
# in the first index we have the operation "Delete:"    "Insert:"   "Update:"
# in the second index we have the position of the node (following the preorder traversal of B ++ where it should be in A)
# in the third index we have the value to integrate



def patching(ES, tree):

    tree_preordered = preorder(tree.getroot())
    print(tree_preordered)
    print(ES)


    for i in range(0, len(ES)): #Looping in SAME order AS the ES (because it follows the backtrace order so the steps are reversed, SO there is DELETION OF A NODE's PARENT BEFORE ITS CHILD)

        if(ES[i][0] == "Delete:"):
          #Step 1: get all elements to remove (because .pop will change their positions // .pop will affect our tree_preordered)
          node_pos = ES[i][1]

          #FOR PRE ORDER PATH
          #print(tree_preordered[node_pos])
          node = tree_preordered[node_pos]  #prints element with its ID
          tree_preordered.remove(node)

          #FOR TREE
          delete(tree.getroot(), node, nested=True)
        
        elif( ES[i][0] == "Insert:" ):
          node = ES[i][1]
          node_pos_parent = ES[i][2]
          parent_node = ES[i][3]
          parent_pos_traversal = ES[i][4]

          # #FOR PRE ORDER PATH
          # if(node_pos > len(tree_preordered)):
          #   for i in range(len(tree_preordered),node_pos):  #without this for loop the function .insert will just set it at the end of the list
          #     tree_preordered.insert(i,'-')       #will be filled in later steps
          #   tree_preordered.insert(node_pos,node)
          # else:
          #   tree_preordered[node_pos] = node
          # #print(tree_preordered)

          #FOR TREE
          insert(tree.getroot(),node,node_pos_parent,parent_node,parent_pos_traversal,nested=True)
          # max = len(preorder(tree.getroot()))-1
          # print("MAX",max)
          # insert(tree.getroot(), node, node_pos,0,max)

#           #Example
# [['Insert:', 7, 'h'], ['Insert:', 6, 'gdppc'], ['Insert:', 5, 'year'], ['Insert:', 4, 'rank']]
# [<Element 'country' at 0x0000023B6C958EF0>, <Element 'rank' at 0x0000023B6C958F40>, <Element 'year' at 0x0000023B6C958FE0>, <Element 'gdppc' at 0x0000023B6C959080>]
# [['Insert:', 7, 'h'], ['Insert:', 6, 'gdppc'], ['Insert:', 5, 'year'], ['Insert:', 4, 'rank']]
# [<Element 'country' at 0x0000021EFFF38F90>, <Element 'rank' at 0x0000021EFFF38FE0>, <Element 'year' at 0x0000021EFFF39080>, <Element 'gdppc' at 0x0000021EFFF39120>]
# [<Element 'country' at 0x0000021EFFF38F90>, <Element 'rank' at 0x0000021EFFF38FE0>, <Element 'year' at 0x0000021EFFF39080>, <Element 'gdppc' at 0x0000021EFFF39120>, '-', '-', '-', <Element 'h' at 0x0000021EFFF39530>]
# [<Element 'country' at 0x0000021EFFF38F90>, <Element 'rank' at 0x0000021EFFF38FE0>, <Element 'year' at 0x0000021EFFF39080>, <Element 'gdppc' at 0x0000021EFFF39120>, '-', '-', <Element 'gdppc' at 0x0000021EFFF39490>, <Element 'h' at 0x0000021EFFF39530>]
# [<Element 'country' at 0x0000021EFFF38F90>, <Element 'rank' at 0x0000021EFFF38FE0>, <Element 'year' at 0x0000021EFFF39080>, <Element 'gdppc' at 0x0000021EFFF39120>, '-', <Element 'year' at 0x0000021EFFF393F0>, <Element 'gdppc' at 0x0000021EFFF39490>, <Element 'h' at 0x0000021EFFF39530>]
# [<Element 'country' at 0x0000021EFFF38F90>, <Element 'rank' at 0x0000021EFFF38FE0>, <Element 'year' at 0x0000021EFFF39080>, <Element 'gdppc' at 0x0000021EFFF39120>, <Element 'rank' at 0x0000021EFFF39350>, <Element 'year' at 0x0000021EFFF393F0>, <Element 'gdppc' at 0x0000021EFFF39490>, <Element 'h' at 0x0000021EFFF39530>]

        elif( ES[i][0] == "Update:" ):
          
          node_del_pos = ES[i][1]
          node_del = tree_preordered[node_del_pos]
          node_ins_pos = ES[i][2]
          node_ins = ES[i][3]

          #FOR PRE ORDER PATH
          tree_preordered[node_del_pos] = node_ins  #both nodes (to insert and delete have the same index #Chawathe condition) + only need val of inserted node
          
          #FOR TREE
          update(tree.getroot(), node_del, node_ins, nested=True)
    
    tree_preordered = preorder(tree.getroot())
    print(tree_preordered)