#program to reverse the string enter by the user
st=input('Enter a string for reversal of the string:')
li=[]
st2=str()
s=st.split(sep=' ')
li=s[::-1]
output=' '.join(li)
print('The string{0} after the reversal is {1}:'.format(st,output))
for ch in range(-1,-(len(s)+1),-1):
    st2+=s[ch]
    st2+=' '
print('The string{0} after the reversal is {1}:'.format(st,st2))
