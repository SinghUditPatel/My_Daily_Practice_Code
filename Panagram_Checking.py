def check_PanaGram(s1):
    b=[0]*26
    for i in s1:
        if(i.islower()):
            b[ord(i)-ord('a')]=1
        else:
            if(i.isupper()):
                i=i.lower()
                b[ord(i)-ord('a')]=1
    for i in range(len(b)):
        if(b[i]!=1):
            return False
    return True
# s ="Bawds jog, flick quartz, vex nymph"
s="sdfs"
print(check_PanaGram(s))
