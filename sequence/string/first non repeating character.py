#program to read all the character from the string and compair this with the actual srting and find the first non repeating character from the string
st=input('Enter a string for operation:')
count=1
for i in range(len(st)):
    print(st[i])
    for j in range(len(st)+1):
        if st[i]==st[j+1]:
            count+=1
        if count>=2:
            break
        else:
            continue
print('The first non repeating character in the string{0} is {1}'.format(st,st[j]))
        
