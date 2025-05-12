def find_Smaillest_Missing_Positive_Number(arr):
    flag=False
    n=len(arr)
    for i in range(len(arr)):
        if(arr[i]==1):
            flag=True
            break
    if flag:
        for i in range(n):
            if arr[i]<1 or arr[i]>n:
                arr[i]=1
        for j in range(n):
            arr[j]-=1
        for k in range(n):
            arr[arr[k]%n]+=n
        for l in range(n):
            if(arr[l]//n==0):
                return l+1
        return n+1
    else:
        return 1
arr=[-8, 0, -1, -4, -3]
print(find_Smaillest_Missing_Positive_Number(arr))   