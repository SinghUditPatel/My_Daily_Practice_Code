def short_Sentenses(s):
    
    b=[0]*10
    temp=""
    n=len(s)
    string=s.split(" ")
    for i in range(len(string)):
        temp=string[i]
        b[int(temp[len(temp)-1])]=temp[:len(temp)-1]
    return " ".join(b[i]  for i in range(len(b)) if b[i]!=0)

s="sentence4 a3 is2 This1"
print(short_Sentenses(s))

#     for i in range(n):
#         if(s[i]>='1'  and s[i]<='9'):
#             if(i!=n-1 and s[i+1]==" "):
#                 b[int(s[i])]=temp
#                 temp=""
#             elif(i==n-1):
#                 b[int(s[i])]=temp
#                 temp=""
#             else:
#                 temp+=s[i]
#         elif(s[i]!=" "):
#             temp+=s[i]
#     temp=""
#     print(b)
#     for i in range(len(b)-1):
#         if(b[i]!=0):
#             temp+=b[i]+" "
#     return temp[:len(temp)-1]


