#program to reverse using while loop
s=input('Enter a sring for operations:')
st=''
i=len(s)-1
while i>=0:
    st+=s[i]
    i-=1
print('The string you have entered is {0} and after reversal is{1}::'.format(s,st))
