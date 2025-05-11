def segre_0_1(arr):
    if(len(arr)<=1):
        return arr
    low=0
    end=len(arr)-1
    while(low<=end):
        if(arr[low]==0):
            low+=1
        else:
            if(arr[end]==0):
                arr[low],arr[end]=arr[end],arr[low]
                low+=1
                end-=1
            else:
                end-=1
    return arr   
arr=[0,0,0,0,0,1,0,1,0,0]
print(segre_0_1(arr))