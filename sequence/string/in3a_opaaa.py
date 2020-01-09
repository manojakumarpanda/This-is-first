#program for input of a4b3c2 the output should be aaaabbbcc
st=input('Enter a string in the format of a3b3::')
st2=''
for ch in st:
    if (ch>='a'and ch<='z')or(ch>='A' and ch<='Z'):
        cha=ch
    elif ch>='0'and ch<='9':
        i=int(ch)
        st2+=cha*i
    else:
        pritn('You have entered a wrong format:')
print('The sring you have entered is {0} and afte converssion the string is{1}'.format(st,st2))
