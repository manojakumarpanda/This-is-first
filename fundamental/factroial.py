#program for the finding factorial of the given number
num=int(input('Enter the number to find factorial of the given number :'))
fix,fact=num,1
if num == 0:
    print('The factorial of the given number is:',fact)
else:
    while num!=0:
        fact=fact*num
        num-=1
print('the factorial of the given number {:d} is :'.format(fix),fact)
# Python program to find the factorial of a number using recursion
def fact (fix):
    rem=1
    if fix==0:
        print('The factorial of the given number is:',rem)
    elif fix==1:
        return fix
    else:
        return fix*fact(fix-1)
res=fact(fix)
print('the factorial of the given number {:d} is :'.format(fix),res)

