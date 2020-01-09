#program for the the reversal of the order of the word

string='pyhton is a programming language'

st=string.split(' ')
inter=[]

for ch in st:
    inter.append(ch[::-1])

output=' '.join(inter)
print('the output of the string "{}" and after the conversion of the string is ::'.format(string),output)


print("*"*50)

#program for the reversal of the order of the word using the while loop

stri='python is a programming language'
s=stri.split(' ')
inte=[]

i=0
while i<len(s):
    inte.append(s[i][::-1])
    i+=1

out=' '.join(inte)
print('the output of the string"{}" and after the conversion of the string is::'.format(stri),out)


print("*"*50)
#programing for the reversla of the content of the string using  
    
