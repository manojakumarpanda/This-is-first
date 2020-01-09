#program to remove a given characher from the given string
st=input('Enter the first string for operations:')
st1=list(st)
st2=input('Enter a character you want remove from the string')
i=0
for ch in st1:
    if ch==st2:
        st1[i]=' '
    i+=1
s=''.join(st1)
print('The string after the removal of the characters form the "{0}"'.format(st2),s)
    
