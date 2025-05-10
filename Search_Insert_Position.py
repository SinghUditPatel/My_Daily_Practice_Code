def find_Apro(arr,key):
    low=0
    end=len(arr)-1
    ans=len(arr)
    while(low<=end):
        mid=low+(end-low)//2
        if(arr[mid]==key):
            return mid
        elif(arr[mid]<key):
            low=mid+1
        else:
            ans=mid
            end=mid-1
    return ans
arr=[1,3,5,6]
key=2
print(find_Apro(arr,key))