def add_2d_Matrix(arr1,arr2):
    b=[[0 for _ in range(len(arr1[0]))]for _ in range(len(arr1))]
    for i in range( len(arr1)):
        for j in range(len(arr1[0])):
            b[i][j]=arr1[i][j]+arr2[i][j]
    return b 
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b1 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(add_2d_Matrix(a,b1))

