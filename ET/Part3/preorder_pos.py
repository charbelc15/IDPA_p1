import xml.etree.ElementTree as ET

def preorder_pos(root):

    if root is None:
        return [] 
    ans = [root,0] #We can add .tag to root but it WILL BECOME A STRINGS array
    for x in root:
        ans += [preorder_pos(x),x]        
    return ans