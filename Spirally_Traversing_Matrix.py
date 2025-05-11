def spirally_Traverse(arr):
    top=0
    bottom=len(arr)-1
    right=len(arr[0])-1
    left=0
    b=[]
    while(top<=bottom and left<=right):
        for i in range(top,bottom+1):
            b.append(arr[top][i])
        top+=1
        for j in range(top,bottom+1):
            b.append(arr[j][right])

        right-=1
        if(top<=bottom):
            for k in range(right,left-1,-1):
                b.append(arr[bottom][k])
            bottom-=1
        if(left<=right):
            for l in range(bottom,top-1,-1):
                b.append(arr[l][left])
            left+=1
    return b
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(spirally_Traverse(mat))
