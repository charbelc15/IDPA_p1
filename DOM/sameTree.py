from logging import root
import xml.etree.ElementTree as ET
import xml.dom.minidom


def sameTree(root1, root2) -> bool:    
    # if both trees are empty : same
    if not root1 and not root2:
        return True

    # one of them is EMPTY the other is NOT EMPTY
    if not root1 or not root2:
        return False

    # if the roots are different
    if root1.tag != root2.tag:
        return False

    #now , both root1 and root2 and not empty       AND         root1 same as root2
    for child_d1 in root1:
        for child_d2 in root2:
            return sameTree(child_d1,child_d2)