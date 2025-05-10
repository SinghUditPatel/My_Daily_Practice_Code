import sys
def max_Sub_Array(arr):
    maxSum=-sys.maxsize
    prefix=0
    for i in range(len(arr)):
        prefix+=arr[i]
        if(prefix>maxSum):
            maxSum=prefix
        if(prefix<0):
            prefix=0
    return maxSum
arr = [5, 4, 1, 7, 8]
print(max_Sub_Array(arr))