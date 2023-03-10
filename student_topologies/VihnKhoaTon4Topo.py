# submitted by Vihn Khoa Ton, OMSCS Fall 2018

## Topology 4 - a candy for anyone who got this far ##
#    2 --- 6    10 --- 15    4 --- 12  # Answer: 2 --- 6    10 --- 15    4     12
#     \     \   / \   / \   /     /    #                \           \   /     /
#      \     \ /   \ /   \ /     /     #                 \           \ /     /
#       9 --- 3 --- 16 -- 7 --- 17     #            9 --- 3 --- 16 -- 7     17
#      /     / \   / \   / \     \     #                 /           / \     \
#     /     /   \ /   \ /   \     \    #                /           /   \     \
#    11 -- 8     14 -- 5     13 -- 1   #         11 -- 8     14 -- 5     13 -- 1
#     
# 

topo = { 1 : [13, 17],                 # Answer: 1 - 13, 1 - 17
         2 : [9, 6],                   #         2 - 6
         3 : [10, 6, 16, 14, 8, 9],    #         3 - 6, 3 - 8, 3 - 9, 3 - 16
         4 : [12, 7],                  #         4 - 7
         5 : [14, 16, 7],              #         5 - 7, 5 - 14
         6 : [2, 3],                   #         6 - 2, 6 - 3
         7 : [15, 16, 4, 17, 5, 13],   #         7 - 4, 7 - 5, 7 - 13, 7 - 15, 7 - 16
         8 : [11, 3],                  #         8 - 3, 8 - 11
         9 : [2, 11, 3],               #         9 - 3
         10 : [3, 15, 16],             #         10 - 15
         11 : [8, 9],                  #         11 - 8
         12 : [17, 4],                 #         12 - 17
         13 : [1, 7],                  #         13 - 1, 13 - 7
         14 : [16, 3, 5],              #         14 - 5
         15 : [10, 7, 16],             #         15 - 7, 15 - 10
         16 : [7, 5, 3, 14, 10, 15],   #         16 - 3, 16 - 7
         17 : [7, 1, 12] }             #         17 - 1, 17 - 12