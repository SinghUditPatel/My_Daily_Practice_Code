def trap_Water(arr):
    rightMax=0
    leftMax=0
    rightIn=0
    waterCap=0
    for i in range(len(arr)):
        if(arr[i]>rightMax):
            rightMax=arr[i]
            rightIn=i
    for i in range(rightIn):
        if(leftMax>arr[i]):
            waterCap+=leftMax-arr[i]
        else:
            leftMax=arr[i]
    rightMax=0
    for i in range(len(arr)-1,rightIn,-1):
        if(rightMax>arr[i]):
            waterCap+=rightMax-arr[i]
        else:
            rightMax=arr[i]
    return waterCap
arr=[2, 1, 5, 3, 1, 0, 4]
print(trap_Water(arr))