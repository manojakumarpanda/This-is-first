#program for the to check a given number is prime number or not
num=int(input('Enter the number to check the number is prime or not:'))
fix,pri,mid=num,0,1
comp=num//2
if num==0 or num==1 :
    print('The number you have entered are special number :')
else:
    while comp<=smid:
        if num%mid==0:
            pri+=1
            mid=mid+1
#if pri >=2:
#    print('The number you have entered{:d} is a prime number:'.format(fix),pri)
#else:
#    print('The number you have entered {:d} is not a prime :'.format(fix),pri)
print(pri)
