def addi():
    a=int(input('Enter the 1st value for the addition operation:'))
    b=int(input('Enter the 2nd value for the addition operation:'))
    add=a+b
    print('The addition of the input value is:',add)
    st=str(input ('Enter the 1st string value for concatination operation:'))
    st2=str(input ('Enter the 2nd string value for concatination operation:'))
    concat=st+st2
    print('The concatination of two input string::',concat)
    return
def sub():
    a=int(input('enter the first value for the substraction operation:'))
    b=int(input('enter the second value for the substraction operation:'))
    sub=a-b
    print('The substraction of two number:',sub)
    return
def div(a,b):
    div=a/b
    return div
def mod():
    a=int(input('enter the first value for the modulardivision operation:'))
    b=int(input('enter the second value for the modulardivision operation:'))
    modu=a%b
    print('The modular division of the given input numbers is:',modu)
    return
def intdiv():
    a=int(input('enter the first value for the intdivision operation:'))
    b=int(input('enter the second value for the intdivision operation:'))
    div1=a//b
    print('The floordivision type of operation in the :',div1)
    return
def power():
    p=int(input("enter the value for the power:"))
    q=int(input('enter the second value for the power or exponentional operation:'))
    r=p**q
    return r
def mul():
    a=int(input('Enter the value for the multification:'))
    b=int(input('Enter another value for the multification:'))
    mul=a*b
    print ('for the out put of the function is given below:',mul)
    st=input('Enter a string for the multification operation:')
    mul1=a*st
    mul2=st*b
    print('the result of the multification of number and string',mul1)
    print('the result of the multification of number and string in differnt format',mul2)
    return
#function call of the different operation of the operator
addi()
sub()
a=int(input('enter the first value for the float division operation:'))
b=int(input('enter the second value for the float division operation:'))
res=div(a,b)
print('the value or the result of the division of the two number is:',res)
print('the value or the result of the division of the two number is:',div(a,b))
mod()
intdiv()
res2=power()
print('the result of the two given number is:',res2)
print('teh result of the two given number is:',power())
mul()

    
    
