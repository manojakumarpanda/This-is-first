#How to check if two string are rotation of each other in'XYZ' and 'ZYX'
st=input('Enter the first string for mirror rotation compairision::')
st2=input('Enter the second string for mirror rotation compairision::')
st3=''
for i in range(-1,-(len(st)+1),-1):
    st3+=st[i]
if st2==st3:
    flag=True
else:
    flag=False
print('Is the two {0} {1} string are mirror rotation of each other::'.format(st,st2),flag)

