#program to reverse the odd place word in the given string
s=input('Enter the string to operate::')
li=s.split(sep=' ')
st=str()
for c in range(len(li)):
    if c%2!=0:
        stt=li[c]
        i=len(stt)-1
        while i>=0:
            st+=stt[i]
            i-=1
        st+=' '
    else:
        continue
lis=li[1:len(li):2]
print('The strint you have entered "{0}" and the odd place strings are "{1}" and after the reverse "{2}"'.format(s,lis,st))
