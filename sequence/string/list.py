l=list=[[1,2,3],[4,5,6]]
for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j]+=10
print(l)
