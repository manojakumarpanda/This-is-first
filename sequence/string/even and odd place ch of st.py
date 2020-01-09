#program to find the even place and the odd plce character seperately
s=input('Enter the string for the operation::')
sp=s.split(sep=' ')
even=[]
odd=[]
for c in sp:
    dup=c
    i=0
    while i<len(c):
        if i%2==0:
            even.append(dup[i])
        else:
            odd.append(dup[i])
        i+=1
print('The  string you heve givn from keyboard {0} and the even place charactes are {1} odd place character are{2}'.format(s,even,odd))
print('The even place string are of the given string::')
for c in sp:
    i=0
    while i<len(c):
        print(c[i])
        i+=2
print('The odd place characte of the string is ::')
for c in sp:
    i=1
    while i<len(c):
        print(c[i])
        i+=2


        
    
