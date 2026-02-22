
a=int(input("Enter a first number:"))
b=int(input("Enter a second number:"))
c=int(input("Enter a third  number:"))
def greatest(a,b,c):
    if(a>b and a>c):
        return("A is greatest")
    elif(b>a and b>c):
        return("B is Greatest ")
    elif(c>a and c>b):
        return("C is greatest")
print(greatest(a,b,c))



    