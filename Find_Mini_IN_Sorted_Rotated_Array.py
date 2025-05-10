def min_Rotared_Array(arr):
    ans=arr[0]
    low=0
    end=len(arr)-1
    while(low<=end):
        mid=low+(end-low)//2
        if(arr[mid]>=arr[0]):
            low=mid+1
        else:
            ans=mid
            end=mid-1
    return ans
arr=[4, 2, 3]
print(arr[min_Rotared_Array(arr)])     