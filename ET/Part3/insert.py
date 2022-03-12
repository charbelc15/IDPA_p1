import xml.etree.ElementTree as ET

def insert(root,node, node_pos,counter,max):
    #print(node_pos)
    print(counter, max, root)
    if root is None:
        return [] 

    
    for x in root:
        if(counter==node_pos or counter==max):
            root.insert(0,ET.SubElement(root,node))
        else:
            counter+=1
            insert(x,node, node_pos,counter,max)        