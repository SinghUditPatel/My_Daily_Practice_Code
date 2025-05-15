def check1(st1,st2):
        if(st1[0]==st2[len(st2)-2] and st1[1]==st2[len(st2)-1]):
            for i in range(len(st1)-2):
                if(st1[i+2]!=st2[i]):
                    return 0
            return 1
                
def isRotated(s1,s2):
        #code here
    if(len(s1)==len(s2)):
            
        # max1=max(self.check(s1,s2),self.check(s2,s1))
        if(check1(s1,s2) or check1(s2,s1) ):
            return True
        else:
            return False
    else:
        return False
s1 = "amazon"
s2 = "azonam"
print(isRotated(s1,s2))