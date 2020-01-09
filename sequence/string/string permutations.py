#program to print the permutation of the the number is eg:123 132 213 231 312 321
num=123
lis=[]
while num!=0:
    lis.append(num%10)
    num=num//10
print(lis)
print('*'*20)

'''def paint(lis,n):
    
    for i in range(3):
        print(lis)
        print()'''
for j in range(3):
    for i in range(2):
        lis[i],lis[i+1]=lis[i+1],lis[i]
        print(lis)
    
