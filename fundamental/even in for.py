#program to print the even number up to n using for loop and range 
num=int(input('Enter the value up which you want to print the even number:'))
su,sub=0,0
for i in range(2,num+1,2):
    print('The all the even number in between the {:d} is :'.format(num),i)
    su=su+i
    sub=sub-i
print('The sum of all the even number is :',su)
print('The substraction of all the even number is :',sub)
