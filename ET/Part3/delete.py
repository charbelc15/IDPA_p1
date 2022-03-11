
#def delete(tree, counter, node_pos, node):
def delete(tree, node):    
    root = tree.getroot()
    for child in root.iter():
        if child != node:
            continue
        if True:# TODO: do your check here!
            root.remove(child)    
    # if root is None:
    #     return [] 
    # ans = [root] #We can add .tag to root but it WILL BECOME A STRINGS array
    # for x in root:
    #     if(counter==node_pos):

    #     counter+=1
    #     ans += delete(x,counter,node_pos,node)        
    # return ans