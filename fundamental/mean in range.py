#program to find the mean of the given range and the range provide by you
num=int(input('Enter the number to find the mean of the range:'))
ran=range(0,11,1)
length=len(ran)
length2=len(range(num))
su,summ=0,0
for i in ran:
    su=su+i
for r in range(num):
    summ+=r
mean1=su//length
mean2=summ//length2
print('The mean of the given range is:',mean1)
print('The mean of the number enter by the user:',mean2)
med=ran[len(ran)//2+1]
print('The median of the given range is :',med)
    
