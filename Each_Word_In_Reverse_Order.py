def reverse_Word(str1):
    str1=str1.split(" ")
    str1=" ".join(i[::-1] for i in str1)
    print(str1)
str1="Hello World"
reverse_Word(str1)