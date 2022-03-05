import xml.dom.minidom

# Gives total number of elements/subtrees: try it out in xml2tree.py
#   M=nbchildren(tree1)
#   N=nbchildren(tree2)


def nbchildren(root):

    Nb_children=0
        

    while(root.hasChildNodes):
        for child in root.childNodes:
            if(child.nodeType == 1):
                Nb_children+=1
            nbchildren(child)        
    
    
    return(Nb_children)