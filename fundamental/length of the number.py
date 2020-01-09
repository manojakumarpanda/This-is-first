#program to find the length of the digit
num=int(input('Enter a number for calculation of the length::'))
count,rem,rev,su,s=0,0,0,num,0
pal=num
nu=num
fix=num
while num!=0:
    num=num//10
    count+=1
print('The length of the number {:d}you have entered:'.format(fix),count)
def comp(nu,rev,rem):
    while nu!=0:
        rem=nu%10
        rev=(rev*10)+rem
        nu=nu//10
    return rev
#this program is to find the sum of the digit
while su!=0:
    rem=su%10
    s=s+rem
    su=su//10
print('The addition of the digits of the number {:d} is ::'.format(fix),s)
#this program is to check for the number is palindrum or not
#this is for the reversal of the number
pal=comp(nu,rev,rem)
print('The reversal of the number {:d} is:'.format(fix),comp(nu,rev,rem))
if nu == pal:
    print('This number you have entered {:d}and reverse of the number {:d} is pallindrum'.format(fix,pal),pal)
else:
    print('This number you have entered {:d} and reverse of the number {:d} is not a pallindrum'.format(fix,pal),pal)

