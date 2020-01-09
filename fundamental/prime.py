#program to find the given number is prime or not by using the break and continue statement
num=int(input('Enter a number to check prime or not:'))
count=0
for i in range(1,num//2):
    if num%i==0:
        count+=1
    if count>2:
        break
    else:
        continue
if count==1:
    print('The number you have entered is a prime number:',num)
else:
    print('The number you have entered is not a prime number:',num)
