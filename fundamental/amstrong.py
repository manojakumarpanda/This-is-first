#program to find the number is amstrong number or not
num=int(input('Enter  a number to check the number is amstrong or not:'))
rem,am,fix=0,0,num
while num!=0:
    rem=num%10
    am=am+rem**3
    num=num//10
if am == fix:
    print('The number you have entered {:d} is a amstrong number ::'.format(fix),am)
else:
    print('The number you have entered {:d} is not a amstrong number::'.format(fix),am)
