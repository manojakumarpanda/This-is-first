#program to make the string with combination of two string character in alternative
st=input('Enter the first string for the operation:')
stt=input('Enter the second string for the operation::')
stalt=str()
i,j=0,0
while i<len(st) or j<len(stt):
    stalt=stalt+(st[i]+stt[j])
    i+=1
    j+=1
print('the first string is"{0}" and the second is "{1}" after the conversion string is "{2}"'.format(st,stt,stalt))

      
