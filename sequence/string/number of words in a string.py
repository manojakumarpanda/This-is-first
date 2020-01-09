#program to find the number of words in the string
string=input('Enter the string for operation::')
count=1
for ch in string:
    if ch==' ':
        count+=1
print('The number of word present in the string is::',count)
st=string.split(' ')
print('The number of word present in the string is::',len(st))
