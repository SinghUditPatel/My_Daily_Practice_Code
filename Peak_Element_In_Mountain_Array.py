def peak_Ele(arr):
    low=0
    end=len(arr)-1
    while(low<=end):
        mid=low+(end-low)
        left=arr[mid-1] if mid>0 else float('-inf')
        right=arr[mid+1] if mid<len(arr)-1 else float('-inf')
        # peak Element
        if(arr[mid]>left and arr[mid]>right):
            return mid
        # right side move
        elif(arr[mid]>left):
            low=mid+1
        # Left side move
        else:
            end=mid-1
    return -1
arr = [1, 2, 4, 5, 7, 8, 3]
print(arr[peak_Ele(arr)])