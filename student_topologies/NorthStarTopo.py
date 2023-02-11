# submitted by Edward, OMSCS Fall 2018
#                         3
#                         |
#                         |
#                        13
#                         |
#                         |
#                14 -- 15 -- 16
#                  |      |       |
#                  |      |       |
# 4 --- 10 --- 9 --- 5 --- 17 --- 12 --- 2
#                  |      |       |
#                  |      |       |
#                  6 --- 7 --- 8
#                          |
#                          |
#                        11
#                          |
#                          |
#                         1

topo = { 1 : [11],
         2 : [12],
         3 : [13],
         4 : [10],
         5 : [7, 9, 15, 17],
         6 : [7, 9],
         7 : [5, 6, 8, 11],
         8 : [7, 17],
         9 : [5, 6, 10, 14],
         10: [4, 9],
         11: [1, 7],
         12: [2, 17],
         13: [3, 15],
         14: [9, 15],
         15: [5, 13, 14, 16],
         16: [15, 17],
         17: [5, 8, 12, 16] }