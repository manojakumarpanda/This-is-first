#program to find the largest pallindrum word in the string
var=input('Enter a string for the operation::')
lis=var.split()
lis1=[]
lis2=[]
for i in lis:
    lis1.append(i[-1:-(len(i)+1):-1])
for i in range(len(lis)):
    for j in range(len(lis1)):
        if lis[i]==lis1[j]:
            lis2.append(lis[i])
        else:
            continue
for c in lis2:
    for d in lis2:
        if len(c)<len(d):
            print(d)
print('The largest pallindrum in the string you have provided is::',d)
    


