two_D_array_row_size = int(5+1)         # . + LD_pairA elements 
two_D_array_column_size = int(6+1)      # . + LD_pairB elements
#Declaring an empty 1D list.
dist = [] #global 
#Declaring an empty 1D list.
first_row = []
first_column = []
#Initialize the column to Zeroes.
for j in range(0, two_D_array_column_size):
    if j==0:
        first_row.append(0)
    else:
        first_column.append(j)
#Append the column to each row.
for i in range(0, two_D_array_row_size):
    if i==0:
        dist.append(b_column)
    else:
        dist.append()

print(dist)
# dist=[]
# dist[0][0] = 0

# for i in range(1, 5+1): # LD_pair_size+1 value excluded
#     print("old:" , dist[i-1][0])
#     dist[i][0]= (dist[i-1][0] + 1) 
#     print("new:" , dist[i][0])
#     #print(i)  

# print(dist)

# print(dist[0][0])