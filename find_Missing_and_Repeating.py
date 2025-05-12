def missing_And_Repeating(arr):
    n=len(arr)
    missing=0
    repeating=0
    for i in range(len(arr)):
        arr[i]-=1
    for j in range(len(arr)):
        arr[arr[j]%n]+=n
    for k in range(len(arr)):
        if(arr[k]//n==2):
            repeating=k+1
        if(arr[k]//n==0):
            missing=k+1
    print(repeating," ",missing)
arr=[1,3,3]
missing_And_Repeating(arr)
