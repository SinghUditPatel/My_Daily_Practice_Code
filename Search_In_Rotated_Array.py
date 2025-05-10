def find_In_Rotated_Array(arr,key):
    low=0
    end=len(arr)-1
    while(low<=end):
        mid=low+(end-low)//2
        if(arr[mid]==key):
            return mid
        elif(arr[mid]>=arr[0]):
            if(arr[low]<=key and arr[mid]>key):
                end=mid-1
            else:
                low=mid+1
        else:
            if(arr[mid]<key and arr[end]>=key):
                low=mid+1
            else:
                end=mid-1 
    return -1  
arr = [5, 6, 7, 8, 9, 10, 1, 2, 3] 
key=10
print(find_In_Rotated_Array(arr,key))