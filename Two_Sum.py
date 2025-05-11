def two_Sum(arr,target):
    low=0
    end=len(arr)-1
    while(low<=end):
        ans=arr[low]+arr[end]
        if(ans==target):
            b=[low,end]
            return b
        elif(ans>target):
            end-=1
        else:
            low+=1
    return False
arr=[2,7,11,15,27]
print(two_Sum(arr,22))