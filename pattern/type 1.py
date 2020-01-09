'''
1         
1 2       
1 2 3     
1 2 3 4   
1 2 3 4 5 '''
for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()
print()
print()
'''1 2 3 4 5 
1 2 3 4   
1 2 3     
1 2       
1         
'''
for i in range(5,0,-1):
    for j in range(1,6):
        if j<=i:
             print(j,end=' ')
        else:
            print(' ',end=' ')
    print()
print()
print()
'''1 2 3 4 5 
  2 3 4 5 
    3 4 5 
      4 5 
        5 '''
for i in range(1,6):
    for j in range(1,6):
        if j>=i:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()
print()
print()
'''5 4 3 2 1 
5 4 3 2   
5 4 3     
5 4       
5         

'''
for i in range(1,6):
    for j in range(5,0,-1):
        if j>=i:
              print(j,end=' ')
        else:
            print(' ',end=' ')
    print()
print()
print()     


'''1 2 3 4 5 
1 2 3 4   
1 2 3     
1 2       
1         '''

for i in range(5,0,-1):
    for j in range(1,6):
        if i>=j:
              print(j,end=' ')
        else:
            print(' ',end=' ')
    print()
print()
print()
'''
        5 
      4 5 
    3 4 5 
  2 3 4 5 
1 2 3 4 5 '''
for i in range(5,0,-1):
    for j in range(1,6):
        if j>=i:
              print(j,end=' ')
        else:
            print(' ',end=' ')
    print()
print()
print()
'''1         
2 3       
4 5 6     
7 8 9 10   
11 12 13 14 15'''
k=1
for i in range(5):
    for j in range(5):
        if j<=i:
               print(k,end=' ')
               k+=1
        else:
            print(' ',end=' ')
    print()
print()
print()
'''1 
1 0 
1 0 1 
1 0 1 0 
1 0 1 0 1 
'''
for i in range(6):
    for j in range(1,i+1):
        if j%2==0:
               print('0',end=' ')
        else:
            print('1',end=' ')
    print()
print()
print()
'''
p           
y y         
t t t       
h h h h     
o o o o o   
n n n n n n '''
s='python'
for i in range(6):
    for j in range (6):
        if j<=i:
            print(s[i],end=' ')
        else:
            print(' ',end=' ')
    print( )
print()
print()
'''
p           
p y         
p y t       
p y t h     
p y t h o   
p y t h o n '''
s='python'
for i in range(6):
    for j in range (6):
        if j<=i:
            print(s[j],end=' ')
        else:
            print(' ',end=' ')
    print( )
print()
print()

