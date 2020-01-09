def add (x,y): #with argument with return value
    sum =x+y #this need to give the same variable as argument as the use in function
    return sum
def mul (x,y): #with argument and no return value
    multification= x*y
    print("the multification of the two number is :",multification)
    return
def divi():  #with no argument and with return value
    print("Enter two number for division program:")
    x=int(input("Enter the first number :"))
    y= int(input('Enter the second number :'))
    res=x/y
    return res
def sub (): # with no argument and no return value
    print ('Enter the two value for substraction operation:')
    x=int(input(print ("Enter the first value:")))# with this statement it will accept the vlaue but will show like Enter the first value and in the next line none
    y=int(input('Enter the second value:'))
    substraction=x-y
    print("this is the substraction of two numbers are :",substraction)
    return
print ("this is the program for the different type of function concept ")
sub () # with no argument and no return value
z=divi()
print ('the division of two number is :',z)#with no argument and with return value
result=add(233,580.55)
print('The addition of two number is :',result)#with argument with return value
mul(30,30)#with argument and no return values
#print('The multification of two numbers is:')  result is showing is The multification of two numbers is: none
