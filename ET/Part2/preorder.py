import xml.etree.ElementTree as ET

def preorder(root):

    if root is None:
        return [] ## TRY IT WITH SPACE DELIMITER HERE FOR LEAF NODES
    ans = [root] #We can add .tag to root but it WILL BECOME A STRINGS array
    for x in root:
        ans += preorder(x)        
    return ans