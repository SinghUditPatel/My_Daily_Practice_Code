def search_in_2D(arr,key):
    low=0
    end=len(arr)*len(arr[0])-1
    while(low<=end):
        mid=low+(end-low)//2
        if(arr[mid//len(arr[0])][mid%len(arr[0])]==key):
            return True
        elif(arr[mid//len(arr[0])][mid%len(arr[0])]<key):
            low=mid+1
        else:
            end=mid-1
    return False
mat = [[18, 21, 27],
                                          [38, 55, 67]]
key=55
print(search_in_2D(mat,key))