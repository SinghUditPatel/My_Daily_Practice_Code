def split(arr):
    if(len(arr)<=1):
        return False
    else:
        sum=0
        for i in range(len(arr)):
            sum+=arr[i]
        prefix=0
        for i in range(len(arr)-1):
            prefix+=arr[i]
            if(prefix==(sum-prefix)):
                return True
        return False
arr = [4, 3, 2, 1]
print(split(arr))