a = int(input("enter no :"))
b = int(input("enter no :"))
c = int(input("enter no :"))
if a>b and b>c:
    print(a)
elif b>a and a>c:
    print(b)
else:
    print(c)