#program for the reverse pyrmaid pattern for the alphabets

'''for the four row patterns
 A B C D 
  A B C 
   A B 
    A '''

row=int(input('Enter the number of row you want to print::'))

for i in range(row):
    print(' '*i,end=' ')
    for j in range(row-i):
        print(chr(65+j),end=' ')
    print()

#programs for the pyramid in the correct format in the "*" or the uper dimond shape 

'''

     *
    * *
  *  *  *
  '''

r=int(input('Enter the value for the number of row you want in the pyramid::'))


for i in range(r):
    print(' '*(r-i-1)+('* '*(i+1)))

#program for the printing of the dimond shape pattern of the lower shape dimond shape


r=int(input('Enter the nomber of the row you want to insert::'))
for i in range(r):
    print(' '*i+'* '*(r-i))


'''
   * 
  * * 
 * * * 
* * * * 
* * * * 
 * * * 
  * * 
   * '''

#programming for the printing of the dimond pattern in star format

n=int(input('Enter the number of row you want to print for the dimond pattern::'))


#for the uper tringle 
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))

#for the lower tringel
    
for i in range(n):
    print(' '*i+'* '*(n-i))



