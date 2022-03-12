
#def delete(tree, counter, node_pos, node):
# def delete(tree, node):    
#     root = tree.getroot()
#     for child in root.iter():
#         if child == node:
#             print(child)
#             child.__delitem__(-1)  


# Hanndle multiple nested levels of tags.
# Does Not delete while forward iterating --> Doesnt l break if multiple xml tags are deleted in the same level one-after-another.
def delete(root, node, nested=False):
    if(root==node):
        root.tag =None
        root.text = None
        root.attrib = {}
    for child in reversed(root):
        if nested:
            if len(child) >= 1:
                delete(child,node)
        if child==node:  
            root.remove(child)
  









    # if root is None:
    #     return [] 
    # ans = [root] #We can add .tag to root but it WILL BECOME A STRINGS array
    # for x in root:
    #     if(counter==node_pos):

    #     counter+=1
    #     ans += delete(x,counter,node_pos,node)        
    # return ans