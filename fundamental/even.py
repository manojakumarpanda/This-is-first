#W.A.P to find number of  even number bellow to the given number
num=int(input('Enter a number for finding the number of the even :'))
i=1
even,count,odd=0,0,0
while i<=num:
    if even%2 == 0:
        print('The number is for even ',even)
        i+=1
        even+=1
        count=count+1
    else:
        print('The number is for odd',even)
        i+=1
        even+=1
        odd=odd+1
print('The number of even number with in the {:d} is equal to== {:d}'.foramt(count,num))
print('The number of odd number with in the {0:d} is equal to== {1:d}'.foramt(odd,num))
