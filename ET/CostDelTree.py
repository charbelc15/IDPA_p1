from logging import root
import xml.etree.ElementTree as ET
from sameTree import sameTree
from subTree import subTree

#cost of deleting tree A(i)
def CostDelTree(treeA, treeB):

    Nb_children=0

    rootA = treeA.getroot()
    rootB = treeB.getroot()
        

    if(subTree(rootA,rootB)): #CHECK if B is subtree of A
        return 1
    else:
        root=treeA.getroot()
        for child in root.iter():
            Nb_children+=1
        return(Nb_children)
        

