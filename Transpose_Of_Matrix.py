def transpose_Mat(arr):
    for j in range(len(arr)):
        for i in range(0,j):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    print(arr)
# mat = [
#         [1, 1, 1, 1],
#         [2, 2, 2, 2],
#         [3, 3, 3, 3],
#         [4, 4, 4, 4]
#     ] 
mat = [
        [1, 2, 3],
        [4, 5, 6]
    ]

transpose_Mat(mat)   