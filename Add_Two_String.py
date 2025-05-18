def calculate(num1,num2):
    l1=len(num1)-1
    l2=len(num2)-1
    ans=""
    carry=0
    for i in range(l1+1):
        if(l2>=0):
            result=int(num1[l1])+int(num2[l2])+carry
            if(result<=9):
                ans=str(result)+ans
                carry=0
            else:
                carry=result//10
                ans=str(result%10)+ans
            l1-=1
            l2-=1
        else:
            result=int(num1[l1])+carry
            if(result<=9):
                ans=str(result)+ans
                carry=0
            else:
                carry=result//10
                ans=str(result%10)+ans
            l1-=1
    return ans
def add_String(num1,num2):
    if(len(num1)>=len(num2)):
        return calculate(num1,num2)
    else:
        return calculate(num2,num1)
# num1 = "11"
# num2 = "123"
num1 = "456"
num2 = "77"
print(add_String(num1,num2))