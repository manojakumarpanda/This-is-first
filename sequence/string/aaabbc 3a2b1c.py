#program for input of aaaabbbcdd output 4a3b1c2d
s=input('Enter the string in the format of aaaabbbcdd:')
li=s.split()
output=' '
li=s[0]
c=1
i=1
#for c in range(i,len(s)):this is with usage of  for loop from 
while i<len(s):
    if s[i]==li:
        c+=1
    else:
        output=output+str(c)+li
        li=s[i]
        c=1
    if i==len(s)-1:
        output=output+str(c)+li
    i+=1
print(output)
