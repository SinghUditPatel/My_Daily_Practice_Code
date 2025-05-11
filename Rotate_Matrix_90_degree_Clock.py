def transpose(arr):
    for i in range(len(arr)):
        for j in range(i):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    return arr
def reverse(arr):
    low=0
    end=len(arr)-1
    while(low<end):
        arr[low],arr[end]=arr[end],arr[low]
        low+=1
        end-=1
    return arr
def rotate_90(arr):

    arr=transpose(arr)
    for i in range(len(arr)):
        arr[i]=reverse(arr[i])
    print(arr)
mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
rotate_90(mat)