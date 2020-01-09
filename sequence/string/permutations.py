#program to print the permutation of the the number is eg:123 132 213 231 312 321
var=input('Enter the number for finding permutation::')
lis=[]
count=0
m=''
v=var.isnumeric()#this will check wether the input is numeric or not


if v==True:#if numeric then go for this if statement
    
    num=int(var)
    while num!=0:
        lis.append(num%10)
        count+=1
        num=num//10
    print(lis)
    print(count)
    print('*'*20)


    for j in range(count):
        for i in range(count-1):
            lis[i],lis[i+1]=lis[i+1],lis[i]
            print(lis)
elif v==False:#if the input string is a string only then go with this
    for ch in var:
      lis.append(ch)
    print(lis)


    for ch in range(len(lis)):
        for c in range(len(lis)-1):
            lis[ch],lis[c]=lis[c],lis[ch]
            m=' '.join(lis)
            print(m)
        
