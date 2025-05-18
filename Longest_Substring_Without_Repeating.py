def find_Len(s):
    b1=set()
    l=0
    end=0
    max_Len=0
    while(end<len(s)):
        if(s[end] not in b1):
           b1.add(s[end])
           max_Len=max(max_Len,end-l+1)
           end+=1

        else:
            while(s[l]!=s[end]):
                b1.remove(s[l])
            
                l+=1

            b1.remove(s[l])
            l+=1
        
    return max_Len

s="abcdecbead"
print(find_Len(s))

        
