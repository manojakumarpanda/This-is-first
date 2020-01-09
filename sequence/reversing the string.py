#program for the reversing the string by using the for loop and the while loop and the slice operator and the slice class
stri=input('Enter the string for the operations::')
st=input('Enter the second string for the operation::')
s=input('Enter the third string for the operations::')
string=input('ENter the fourth string for the operations::')


#by using the for loop
output=''
for i in range(len(stri)-1,-1,-1):
    output+=stri[i]
print('the output of the string "{}" and after the reversing the strig is::'.format(stri),output)


print("*"*50)
#by using the while loop and st
op=''
i=len(st)-1
while i>=0:
    op+=st[i]
    i-=1
print('the output of the string "{}" and afte the conversion and the reversing of the sting is::'.format(st),op)


print("*"*50)
#by using the sliceing operator and the sliceing class

sli=slice(len(s)-1,-len(s)-1,-1)
out=s[sli]
print('the output of the string "{}" and after the conversion and the reversal of the string is::'.format(s),s[sli])

print('*'*50)

outp=string[::-1]
print('the output of the string "{}" and after the conversion and the reversal of the string is ::'.format(string),outp)




