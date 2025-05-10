def missing_Pos(arr,k):
    low=0
    end=len(arr)-1
    ans=len(arr)
    while(low<=end):
        mid=low+(end-low)//2
        if(arr[mid]-mid-1>=k):
            ans=mid
            end=mid-1
        else:
            low=mid+1
    return ans+k
arr = [2,3,4,7,11]
k = 5
print(missing_Pos(arr,k))