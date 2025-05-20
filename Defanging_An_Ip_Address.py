def defanging(s):
    b=""
    for i in s:
        if(i=="."):
            b+="[.]"
        else:
            b+=i
    return b
s="1.2.3.4"
print(defanging(s))
