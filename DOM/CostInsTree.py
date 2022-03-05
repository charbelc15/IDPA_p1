from logging import root
from sameTree import sameTree
from subTree import subTree
import xml.dom.minidom

#cost of inserting tree B(i)
def CostInsTree(treeA, treeB):

    Nb_children=0

    rootA = treeA.firstChild
    rootB = treeB.firstChild
        

    if(subTree(rootA,rootB)): #CHECK if B is subtree of A
        return 1
    else:
        root=treeB.firstChild
        for child in root.childNodes:
            Nb_children+=1
        return(Nb_children)
        


