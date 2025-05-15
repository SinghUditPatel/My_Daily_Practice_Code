def reverse_Order(str1):
    str1=str1[::-1]
    str1=" ".join(i for i in str1)
    print(str1)
s="Hello world"
reverse_Order(s.split(" "))