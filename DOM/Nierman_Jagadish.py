from math import dist
import xml.dom.minidom


def TED(tree1, tree2):
                                                                                     
                                                                                     # 1) M and N
    root1 = tree1.firstChild
    root2 = tree2.firstChild

    Nb_children1=0
    Nb_children2=0

    for child in root1.childNodes:
        Nb_children1+=1

    for child in root2.childNodes:
        Nb_children2+=1

    M=Nb_children1
    N=Nb_children2

    print(M)
    print(N)

                                                                                    # 2) dist

                                                                                    #empty 2D dist matrix

    two_D_array_row_size = int(M)
    two_D_array_column_size = int(N)
    #Declaring an empty 1D list.
    dist = []
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
    print(dist)

                                                                                        # 3) dist[0][0]

    if(root1==root2):
        dist[0][0]=0
    else:
        dist[0][0]=1

                                                                                        # 4) first row - first column

    for i in range(1, M+1): # M+1 excluded
        break
        # Cost of edit operations 1
        # Cost of deleting Ai
        # dist[i][0]=dist[i-1][0] + CostDelTree(Ai)

    for j in range(1, N+1): # N+1 excluded
        break
        # Cost of edit operations 2
        # Cost of Inserting Bi
        # dist[0][j]=dist[0][j-1] + CostInsTree(Bj)


                                                                                            # 5) Rest of Matrix
    
    for i in range(1, M+1):
        for j in range(1, N+1):
            break 
            #dist[i][j]= min(
                # dist[i-1][j-1] + TED( A subtree i, B subtree j ),
                # dist[i-1][j] + CostDelTree(Ai)
                # dist[i][j-1] + CostInsTree(Bj)
            #)
    
    return dist[M-1][N-1]