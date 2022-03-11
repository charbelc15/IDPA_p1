from Part2.preorder import preorder
import xml.etree.ElementTree as ET

from Part3.inv_preorder import inv_preorder

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
    #print(tree_preordered)
    #print(ES)

    To_Delete=[]
    i = len(ES) 
    for i in range(0, len(ES)): #Looping in SAME order AS the ES (because it follows the backtrace order so the steps are reversed, SO there is DELETION OF A NODE's PARENT BEFORE ITS CHILD)

        if(ES[i][0] == "Delete:"):
          #Step 1: get all elements to remove (because .pop will change their positions // .pop will affect our tree_preordered)
          node_pos = ES[i][1]
          print(tree_preordered[node_pos])
          node = tree_preordered[node_pos]
          tree_preordered.remove(node)
        
        elif( ES[i][0] == "Insert:" ):
          node = ES[i][2]
          node_pos = ES[i][1]
          if(node_pos > len(tree_preordered)):
            for i in range(len(tree_preordered),node_pos):  #without this for loop the function .insert will just set it at the end of the list
              tree_preordered.insert(i,'-')       #will be filled in later steps
            tree_preordered.insert(node_pos,node)
          else:
            tree_preordered[node_pos] = node
          #print(tree_preordered)

#           #Example
# [['Insert:', 7, 'h'], ['Insert:', 6, 'gdppc'], ['Insert:', 5, 'year'], ['Insert:', 4, 'rank']]
# [<Element 'country' at 0x0000023B6C958EF0>, <Element 'rank' at 0x0000023B6C958F40>, <Element 'year' at 0x0000023B6C958FE0>, <Element 'gdppc' at 0x0000023B6C959080>]
# [['Insert:', 7, 'h'], ['Insert:', 6, 'gdppc'], ['Insert:', 5, 'year'], ['Insert:', 4, 'rank']]
# [<Element 'country' at 0x0000023B6C958EF0>, <Element 'rank' at 0x0000023B6C958F40>, <Element 'year' at 0x0000023B6C958FE0>, <Element 'gdppc' at 0x0000023B6C959080>, '-', '-', '-', 'h']
# [<Element 'country' at 0x0000023B6C958EF0>, <Element 'rank' at 0x0000023B6C958F40>, <Element 'year' at 0x0000023B6C958FE0>, <Element 'gdppc' at 0x0000023B6C959080>, '-', '-', 'gdppc', 'h']
# [<Element 'country' at 0x0000023B6C958EF0>, <Element 'rank' at 0x0000023B6C958F40>, <Element 'year' at 0x0000023B6C958FE0>, <Element 'gdppc' at 0x0000023B6C959080>, '-', 'year', 'gdppc', 'h']
# [<Element 'country' at 0x0000023B6C958EF0>, <Element 'rank' at 0x0000023B6C958F40>, <Element 'year' at 0x0000023B6C958FE0>, <Element 'gdppc' at 0x0000023B6C959080>, 'rank', 'year', 'gdppc', 'h']
# [<Element 'country' at 0x0000023B6C958EF0>, <Element 'rank' at 0x0000023B6C958F40>, <Element 'year' at 0x0000023B6C958FE0>, <Element 'gdppc' at 0x0000023B6C959080>, 'rank', 'year', 'gdppc', 'h']

        elif( ES[i][0] == "Update:" ):
          
          node_del_pos = ES[i][1]
          node_del = tree_preordered[node_del_pos]
          node_ins = ES[i][2]
          node_ins_pos = ES[i][1]
          tree_preordered[node_del_pos] = node_ins  #both nodes (to insert and delete have the same index #Chawathe condition) + only need val of inserted node


    #print(tree_preordered)    
