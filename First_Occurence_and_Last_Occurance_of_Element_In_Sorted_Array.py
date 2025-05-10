def first_Occurence(arr,key):
    low=0
    end=len(arr)-1
    ans=-1
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

def last_Occurence(arr,key):
    low=0
    end=len(arr)-1
    ans=-1
    while(low<=end):
        mid=low+(end-low)//2
        if(arr[mid]==key):
            ans=mid
            low=mid+1
        elif(arr[mid]<key):
            low=mid+1
        else:
            end=mid-1
    return ans
    



def first_And_Last_Occurence(arr,key):
    b=[0]*2
    if(len(arr)==0):
        return -1
    elif(len(arr)==1):
        if(arr[0]==key):
            return b
        else:
            return -1
    else:
        b1=first_Occurence(arr,key)
        if(b1!=-1):
            b2=last_Occurence(arr,key)
            b[0]=b1
            b[1]=b2
            return b
        else:
            return -1
arr=[5,7,7,8,8,10]
key=10
print(first_And_Last_Occurence(arr,key))        
    
            
    
