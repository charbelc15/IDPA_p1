
def update(root, node_del, node_ins, nested=False):
    if(root==node_del):
        root.tag = node_ins.tag
        if(node_ins.text != None and node_ins.attrib != None):
            root.text = node_ins.text
            root.attrib = node_ins.attrib
        
    for child in reversed(root):
        if nested:
            if len(child) >= 1:
                update(child,node_del, node_ins)
        if child==node_del:
            child.tag = node_ins.tag
            if(node_ins.text != None and node_ins.attrib != None):
                child.text = node_ins.text
                child.attrib = node_ins.attrib
                