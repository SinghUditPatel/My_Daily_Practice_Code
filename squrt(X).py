def sqt(x):
    low=1
    end=x
    ans=0
    while(low<=end):
        mid=low+(end-low)
        if(mid*mid==x):
            return mid
        elif(mid*mid>x):
            end=mid-1
        else:
            ans=mid
            low=mid+1
    return ans
print(sqt(1500))
