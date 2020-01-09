#program to reverse content of each word in the string
s=input('Enter the string to reverse the content of the word::')
li=s.split(sep=' ')
st=''
for c in li:
    x=c
    i=len(x)-1
    while i>=0:
        st+=x[i]
        i=i-1
    st+=' '
dt=' '.join(lis)
print('the string{0} you have givn after the conversion {1}'.format(s,st))
        
        
        
