#identity operators exercise
a=[1,2,3]
b=a
result=b is a # is identity operators
print("result of",b, "is",a,"is :",result)


a=[1,2,3]
b=[4,5,6]
result=b is a # is identity operator
print("result of",b, "is",a,"is :",result)

a=[1,2,3]
b=a 
result=b is a #is identity operator
print("result of ",b, "is not",a,"is :",result)

a=[1,2,3]
b=[1,2,3]
result=b is a # is identity operator
print("result of",b, "is not ",a,"is :",result)
