def convert_Camel_To_Snake(str1):
    str2=""
    for i in range(len(str1)):
        if(str1[i]>='A' and str1[i]<='Z'):
            str2+="_"+chr(ord(str1[i])+32)
        else:
            str2+=str1[i]
    print(str2)
str1="helloHowAreYou"
convert_Camel_To_Snake(str1)