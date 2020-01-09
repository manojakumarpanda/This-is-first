#remove the character from first string presnt in the second string
st=input('Enter the first string for compairision:')
st2=input('Enter the second string for the compairision:')
st3=str()
for ch in st2:
    if ch in st:
        st3+=ch
print('The characters in first string and second string ::',st3)
