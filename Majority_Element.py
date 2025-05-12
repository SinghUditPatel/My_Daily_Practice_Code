def majority(arr):
    candidate=0
    count=0
    for i in range(len(arr)):
        if(count==0):
            candidate=arr[i]
            count+=1
        else:
            if(arr[i]==candidate):
                count+=1
            else:
                count-=1
    count=0
    for j in range(len(arr)):
        if(arr[j]==candidate):
            count+=1
    if(count>(len(arr)//2)):
        print(candidate)
    else:
        print(0)
arr=[2,2,1,1,1,2,2]
majority(arr)