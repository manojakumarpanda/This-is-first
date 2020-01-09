#program to take a n*n matrics and print all the uper matrics and lower matrics and diogna matrics
m=int(input('Enter the number of row and collumn in to the matrixs::'))
mat=[]
i=0
while i<m:
    mat.append([])
    i+=1
for i in range(m):
    for j in range(m):
        ele=int(input('Enter a element for the matrxs mat[{0}][{1}]'.format(i,j)))
        mat[i].append(ele)
for i in range(m):
    for j in range(m):
        if i<=j:
            print(mat[i][j],end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(m):
    for j in range(m):
        if j<=i:
               print(mat[i][j],end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(m):
    for j in range(m):
        if j==i:
               print(mat[i][j],end=' ')
        else:
            print(' ',end=' ')
    print()
        
