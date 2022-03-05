import xml.dom.minidom

from nbchildren import nbchildren


tree1 = xml.dom.minidom.parse("test1.xml") #this gets the file into a tree structure
tree2 = xml.dom.minidom.parse("test2.xml") #this gets the file into a tree structure

#print(tree1.nodeName) # #document
#print(tree1.firstChild) # 

tree1_root=tree1.firstChild
tree2_root=tree2.firstChild


print(nbchildren(tree2_root))

#part 4 done but have to create file 
newXML1 = tree1.toxml()
text_file1 = open("new_Test1.xml", "w")
n1 = text_file1.write(newXML1)
text_file1.close()

newXML2 = tree2.toxml()
text_file1 = open("new_Test2.xml", "w")
n1 = text_file1.write(newXML2)
text_file1.close()