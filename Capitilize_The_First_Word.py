def capi(str1):
    for i in range (len(str1)):
        str1[i]=str1[i].title()
    str1=" ".join(str1)
    print(str1)
str1="python is good"
str1=str1.split(" ")
str1=" ".join(i.title() for i in str1)
# capi(str1)
print(str1)