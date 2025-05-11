import sys

def find_In_Max_Row(arr):
    maxSum=-sys.maxsize
    maxIn=-1
    for i in range(len(arr)):
        sum=0
        for j in range(len(arr[0])):
            sum+=arr[i][j]
        if(sum>maxSum):
            maxSum=sum
            maxIn=i
    return maxIn+1

arr=[[1,2,3],[4,2,1],[5,6,7]]
print(find_In_Max_Row(arr))
