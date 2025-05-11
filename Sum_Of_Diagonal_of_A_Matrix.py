def sum_diagonal(arr):
    firsrDia=0
    secondDia=0
    if(len(arr)==len(arr[0])):
        for i in range(len(arr)):
            firsrDia+=arr[i][i]
        i=0
        j=len(arr[0])-1
        while(j>=0):
            secondDia+=arr[i][j]
            i+=1
            j-=1
        print("PrincipleDiagonal= ",firsrDia," Secondary Diagonal= ",secondDia)
        return 0
    return -1
a= [[ 1, 2, 3, 4 ],[ 5, 6, 7, 8 ], [ 1, 2, 3, 4 ],[ 5, 6, 7, 8 ]]
sum_diagonal(a)

        
