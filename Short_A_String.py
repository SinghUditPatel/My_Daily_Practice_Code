def sort_String(s1):
    b=[0]*26
    s2=""
    for i in s1:
        b[ord(i)-ord('a')]+=1
    for j in range(len(b)):
        for k in range(b[j]):
            s2+=chr(j+ord('a'))
    return s2
S ="edcab"
print(sort_String(S))
