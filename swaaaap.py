def swap(a,b):
    t=a
    a=b
    b=t
    print("value inside function=",a,b)
    return
    
a=int(input("enter a"))
b=int(input("enter b"))
swap(a,b)
print("value outside fun=",a,b)
