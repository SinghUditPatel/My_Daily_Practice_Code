arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target=15
l=0
r=-1
n=len(arr)-1
sum1=0
s=0
while(r<n):
    r+=1
    sum1+=arr[r]
    
    if(sum1>=target):
        
        while(sum1>target and r>l ):
            sum1-=arr[l]
            l+=1
            # print(l)
        if(sum1==target):
            # print(sum1)
            print(l+1," and ",r+1) 
            break 
            
      
