def Sort_Vowel_InString(s):
    b=list(s)
    lower=[0]*26
    upper=[0]*26
    stringVo=""
    for i in range(len(b)):
        if(b[i]=='a' or b[i]=='e' or b[i]=='i' or b[i]=='o' or b[i]=='u' ):
            lower[ord(b[i])-ord('a')]+=1
            b[i]='#'
        elif(b[i]=='A' or b[i]=='E' or b[i]=='I' or b[i]=='O' or b[i]=='U'  ):
            upper[ord(b[i])-ord('A')]+=1
            b[i]='#'
    
    
    for k in range(26):
        char=chr(k+ord('A'))
        for j in range(upper[k]):
            
           
            stringVo+=char
    
    for i in range(26):
        char=chr(i+ord('a'))
        for j in range(lower[i]):
            stringVo+=char
    # print(stringVo)
   
    l=0
    for i in range(len(b)):
        if(b[i]=='#'):
            b[i]=stringVo[l]
            l+=1
    return "".join(b)

s = "lEetcOde"
print(Sort_Vowel_InString(s))