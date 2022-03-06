import xml.etree.ElementTree as ET
from CostInsTree import CostInsTree
from CostDelTree import CostDelTree
from getSubTree import getSubTree

global dist

def TED(tree1, tree2):
                                                                                     
                                                                                     # 1) M and N
    root1 = tree1.getroot()
    root2 = tree2.getroot()

    Nb_children1=0
    Nb_children2=0

    #1st level Children tree list of A (only need 1st cause this is recursive)
    for child in root1:
        Nb_children1+=1

    #1st level Children tree list of B (only need 1st cause this is recursive)
    for child in root2:
        Nb_children2+=1

    M=Nb_children1
    N=Nb_children2

    print(M)
    print(N)

                                                                                    # 2) dist

                                                                                    #empty 2D dist matrix

    two_D_array_row_size = int(M+1)         #R(A) + M children 
    two_D_array_column_size = int(N+1)      #R(B) + N children
    #Declaring an empty 1D list.
    dist = [] #global 
    #Declaring an empty 1D list.
    b_column = []
    #Initialize the column to Zeroes.
    for j in range(0, two_D_array_column_size):
        b_column.append(0)
    #Append the column to each row.
    for i in range(0, two_D_array_row_size):
        dist.append(b_column)
    # 2D array is created.
    #Print the two dimensional list.
    #print(dist)

                                                                                        # 3) dist[0][0]

    if(root1==root2):
        dist[0][0]=0
    else:
        dist[0][0]=1

                                                                                        # 4) first row - first column

    A = getSubTree(tree1) #1st level Children tree list of A (only need 1st cause this is recursive)
    for i in range(1, M+1): # M+1 excluded
        treeA=ET.ElementTree()
        treeA._setroot(A[i-1])  #SUBTREE A1 here is at position 0 of the children's trees list
        dist[i][0]=dist[i-1][0] + CostDelTree(treeA, tree2)  # Cost of deletingAi (going down)



    B = getSubTree(tree2) #1st level Children tree list of B (only need 1st cause this is recursive)
    for j in range(1, N+1): # N+1 excluded
        treeB=ET.ElementTree()
        treeB._setroot(B[j-1])
        dist[0][j]=dist[0][j-1] + CostInsTree(tree1, treeB) # Cost of Inserting Bi (going right)


                                                                                            # 5) Rest of Matrix
    
    for i in range(1, M+1): #M+1 excluded
        treeA=ET.ElementTree()
        treeA._setroot(A[i-1])
        for j in range(1, N+1): #N+1 excluded
            treeB=ET.ElementTree()
            treeB._setroot(B[j-1])
            dist[i][j]= min(
                dist[i-1][j-1] + TED( treeA, treeB ),
                dist[i-1][j] + CostDelTree(treeA, tree2),
                dist[i][j-1] + CostInsTree(tree1, treeB)
            )
    print(dist)
    return dist[M][N]