a=10
b=20
c=30
d=40
e=50
f,g,h,i,j=input('Enter the five integeer value for different operation with space in between:').split(' ')
f=int(f)
g=int(g)
h=int(h)
i=int(i)
j=int(j)
su=a+b+c+d+e
sub=su-f-g-h-j-i
print('sum of the variable {0},{1},{2},{3},{4} is :{5}'.format(a,b,c,d,e,su))
print(' the substraction is of the variable{0},{1},{2},{3},{4} is:{5}'.format(f,g,h,i,j,sub),sep='***')
print('the vlaue of the variable {0:} in the decimal format is:{1:d}'.format(a,b))
print('the value of the variable {0:f},{1:d},{2:o},{3:x},{4:X},{5:b} are'.format(a,b,c,d,e,f))
print('the value of the variable {0:f},{1:d},{2:o},{3:x},{4:X},{5:b} are'.format(g,h,i,j,f,a))

