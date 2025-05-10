def binary_Search(arr,key):
    if(len(arr)==0):
        return -1
    elif(len(arr)==1):
        if(arr[0]==key):
            return 0
        else:
            return -1
    else:
        low=0
        ans=-1
        end=len(arr)-1
        while(low<=end):
            mid=low+(end-low)//2
            if(arr[mid]==key):
                ans=mid
                end=mid-1
                
            elif(arr[mid]<key):
                low=mid+1
            else:
                end=mid-1
        return ans
arr=[1, 1, 1, 1, 2]
key=1
print(binary_Search(arr,key))