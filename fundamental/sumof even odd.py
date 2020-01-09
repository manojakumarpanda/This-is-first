# program for addition of all even number and all odd number that are there in betten of n
num=int(input('Enter the value of n:'))
counte,counto,inc=0,0,0
even,odd,evi=0,0,2
while inc<=num:
    if inc%2==0:
        inc+=1
        counte+=1
        even+=inc
    else:
        odd+=inc
        inc=inc+1
        counto+=1
print('The sum of all the even number is and the number of the even number in between is :',even,counte,sep='-->')
print('The sum of all the odd number is and the number of the odd number in between is:',odd,counto,sep='==>')
#Another way of finding the even number in between n
while evi<=num:
    print('The even number in between {:d} is '.format(num),evi)
    evi+=2












        
