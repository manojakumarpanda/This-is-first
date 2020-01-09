#program to remove all the duplicate in a string and also print the first non repeating and all the duplicate characters
st=input('Enter  a string for the operations:')
st2=''
st3=''
st4=''
count=0
for ch in st:
    if ch in st2:
        st4+=ch
        pass
    else:
        st2+=ch
print('The string you have entered is {0} after removal of the duplicate the string is:{1}'.format(st,st2))
l=list(set(st4))
print('The duplicate character in the given string is:',l)
for ch in st:
    if ch in st3:
        count+=1
    if count<2:
        break
print('The first non repeating character is ::',ch)
