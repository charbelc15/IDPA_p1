



from Part2.preorder import preorder
from Part3.position import position


def insert(root,     node,   node_pos_parent,    parent_node,  parent_pos_traversal   , nested=False):
    
    if(root.tag==parent_node.tag and parent_pos_traversal==0):
        #root is my parent --> insert the node as a subelement
        root.insert(node_pos_parent, node)
    for child in reversed(root):
        child_pos_traversal=position(root,child)
        if nested:
            if len(child) >= 1:
                insert(child, node, node_pos_parent, parent_node, parent_pos_traversal)
        if (child.tag ==parent_node.tag and (child_pos_traversal==parent_pos_traversal)):  
            child.insert(node_pos_parent, node)





# def insert(root,node, node_pos,counter,max):
#     #print(node_pos)
#     print(counter, max, root)
#     if root is None:
#         return [] 

    
#     for x in root:
#         if(counter==node_pos or counter==max):
#             root.insert(0,ET.SubElement(root,node))
#         else:
#             counter+=1
#             insert(x,node, node_pos,counter,max)        