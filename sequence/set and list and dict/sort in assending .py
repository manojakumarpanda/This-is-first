n=int(input('Enter the number of integer you want to insert in the list::'))
lis=[]
for i in range(n):
     lis.append(int(input('Enter the element for the sort in assending order::')))
t=lis
l=len(lis)
for i in range(l):
    for j in range(i,l):
        if lis[i]<lis[j]:
            lis[i],lis[j]=lis[j],lis[i]
print(lis)
