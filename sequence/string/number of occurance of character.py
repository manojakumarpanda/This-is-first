#program to find the number of occurance of acharacter in a string
s=input('Enter a string for manipulation::')
ch=input('Enter a string for finding number of occurance::')
count=0
for c in s:
    if ch==c:
        count+=1
    else:
        continue
print('The character "{0}"you have entered is repeated for "{1}" times::'.format(ch,count),ch*count)
