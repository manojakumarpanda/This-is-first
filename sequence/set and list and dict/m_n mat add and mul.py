#program to print a m*n matrixs  and add them and multiply them
m=int(input('Enter the number of row of the matrixcs::'))
n=int(input('Enter the number of the column in the matrixs::'))
mat=[]
mat2=[]
output=[]
i=0
while i<m:
    mat.append([])
    i+=1
i=0
while i<n:
    mat2.append([])
    i+=1
i=0
while i<n:
    output.append([])
    i+=1
print(mat,mat2,output)
print('Enter the elemet in to the column  of the matrixs mat:')
for i in range(m):
    for j in range(n):
        e=int(input('Enter a element for the matrixs of [{0}][{1}]'.format(i,j)))
        mat[i].append(e)
print('Enter the element fot the collumn of  matrixs mat2::') 
for i in range(m):
    for j in range(n):
        e=int(input('Enter a element for the matrixs2 of [{0}][{1}]'.format(i,j)))
        mat2[i].append(e)        
for i in range(m):
    for j in range(n):
        output[i].append(mat[i][j]//mat2[i][j])
for i in range(m):
    for j in range(n):
        print('The matrixs of the element is mat[{0}][{1}]::'.format(i,j),mat[i][j],sep=' ')
    print()
for i in range(m):
    for j in range(n):
        print('The matrixs of the element is mat2[{0}][{1}]::'.format(i,j),mat2[i][j],sep=' ')
    print()
for i in range(m):
    for j in range(n):
        print('The matrixs after the int division is output[{0}][{1}]:'.format(i,j),output[i][j],sep=' ')
    print()
print(output)

