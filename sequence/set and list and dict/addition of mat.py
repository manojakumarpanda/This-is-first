#program to find sum of n*n matrixs
n=int(input('Entre number of row and coolumn for the marrixs:'))
mat=[]
mat2=[]
i=0
while i<n:
    mat.append([])
    i+=1
print(mat)
print('Enter number of row and coulumn element of the matrixs{0}'.format(i))
for i in range(n):#this loop is for the number of row 
    for j in range(n):#this loop is for the fiiling the element for the column of the mat[i]
        e=int(input('Enter the element for the matrixs of mat[{0}][{1}]'.format(i,j)))
        mat[i].append(e)
i=0   
while i<n:
    mat2.append([])
    i+=1
print(mat2)
print('Enter number of row and coulumn element of the matrixs{0}'.format(i))
for i in range(n):#this loop is for the number of row 
    for j in range(n):#this loop is for the fiiling the element for the column of the mat[i]
        e=int(input('Enter the element for the matrixs of mat2[{0}][{1}]'.format(i,j)))
        mat2[i].append(e)
def add_mat(mat,mat2,n):
    addmat=[]
    i=0
    while i<n:
        addmat.append([])
        i+=1
    for i in range(n):
        for j in range(n):
            addmat[i].append(mat[i][j]+mat2[i][j])
    for i in range(n):
        for j in range(n):
            print('the mat is the as mat[{0}][{1}]:'.format(i,j),mat[i][j],end=' ')
        print()
    for i in range(n):
        for j in range(n):
            print('the mat is the as mat2[{0}][{1}]:'.format(i,j),mat2[i][j],end=' ')
        print()
    for i in range(n):
        for j in range(n):
            print('the addition of two matrix is  addmat[{0}][{1}]:'.format(i,j),addmat[i][j],end=' ')
        print()
def add_sub(mat,mat2,n):
    submat=[]
    i=0
    while i<n:
        submat.append([])
        i+=1
    for i in range(n):
        for j in range(n):
            submat[i].append(mat[i][j]-mat2[i][j])
    for i in range(n):
        for j in range(n):
            print('the mat is the as mat[{0}][{1}]:'.format(i,j),mat[i][j],end=' ')
        print()
    for i in range(n):
        for j in range(n):
            print('the mat is the as mat2[{0}][{1}]:'.format(i,j),mat2[i][j],end=' ')
        print()
    for i in range(n):
        for j in range(n):
            print('the addition of two matrix is  addmat[{0}][{1}]:'.format(i,j),submat[i][j],end=' ')
        print()
def add_mul(mat,mat2,n):
    mulmat=[]
    i=0
    while i<n:
        mulmat.append([])
        i+=1
    for i in range(n):
        for j in range(n):
            mulmat[i].append(mat[i][j]*mat2[i][j])
    for i in range(n):
        for j in range(n):
            print('the mat is the as mat[{0}][{1}]:'.format(i,j),mat[i][j],end=' ')
        print()
    for i in range(n):
        for j in range(n):
            print('the mat is the as mat2[{0}][{1}]:'.format(i,j),mat2[i][j],end=' ')
        print()
    for i in range(n):
        for j in range(n):
            print('the addition of two matrix is  addmat[{0}][{1}]:'.format(i,j),mulmat[i][j],end=' ')
        print()
def add_div(mat,mat2,n):
    divmat=[]
    i=0
    while i<n:
        divmat.append([])
        i+=1
    for i in range(n):
        for j in range(n):
            divmat[i].append(mat[i][j]//mat2[i][j])
    for i in range(n):
        for j in range(n):
            print('the mat is the as mat[{0}][{1}]:'.format(i,j),mat[i][j],end=' ')
        print()
    for i in range(n):
        for j in range(n):
            print('the mat is the as mat2[{0}][{1}]:'.format(i,j),mat2[i][j],end=' ')
        print()
    for i in range(n):
        for j in range(n):
            print('the addition of two matrix is  addmat[{0}][{1}]:'.format(i,j),divmat[i][j],end=' ')
        print()
def add_flot(mat,mat2,n):
    fdivmat=[]
    i=0
    while i<n:
        fdivmat.append([])
        i+=1
    for i in range(n):
        for j in range(n):
            fdivmat[i].append(mat[i][j]/mat2[i][j])
    for i in range(n):
        for j in range(n):
            print('the mat is the as mat[{0}][{1}]:'.format(i,j),mat[i][j],end=' ')
        print()
    for i in range(n):
        for j in range(n):
            print('the mat is the as mat2[{0}][{1}]:'.format(i,j),mat2[i][j],end=' ')
        print()
    for i in range(n):
        for j in range(n):
            print('the addition of two matrix is  addmat[{0}][{1}]:'.format(i,j),fdivmat[i][j],end=' ')
        print()
def mod_mat(mat,mat2,n):
    modmat=[]
    i=0
    while i<n:
        modmat.append([])
        i+=1
    for i in range(n):
        for j in range(n):
            modmat[i].append(mat[i][j]+mat2[i][j])
    for i in range(n):
        for j in range(n):
            print('the mat is the as mat[{0}][{1}]:'.format(i,j),mat[i][j],end=' ')
        print()
    for i in range(n):
        for j in range(n):
            print('the mat is the as mat2[{0}][{1}]:'.format(i,j),mat2[i][j],end=' ')
        print()
    for i in range(n):
        for j in range(n):
            print('the addition of two matrix is  addmat[{0}][{1}]:'.format(i,j),moddmat[i][j],end=' ')
        print()
while True:
    print('Select a option for the operation on the matrixs:')
    print('Enter 1.)for Additon operation {0} 2.)for Substraction {1} 3.)for multification {2} 4.) for division {3} 5.) for float division 6.)for modular division{4}'.format(\n,\n,\n,\n,\n))
    opt=int(input('Enter a option for the mathmatical operations::'))
    break
    print(




