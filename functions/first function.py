#programs on the functions
def fun():  #function defination of type no argument and no return value
    s=int(input('Enter the first number for the operation :'))
    n=int(input('Enter the second number for the operations:'))
    print('The out put of the two number {0}+{1} is::'.format(s,n),s+n)
def fun2():
    s=float(input('Enter the first value for the operation :'))
    n=float(input('Enter the second number for the operation:'))
    d=s*n
    print('The product of the two given number is {0}*{1} is {2:010.2f}:'.format(s,n,d))
def main():
    #fun()#function call
    fun2()#function2 calling statement
main()
