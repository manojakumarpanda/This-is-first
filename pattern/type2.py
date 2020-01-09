'''
1         
2 2       
3 3 3     
4 4 4 4   
5 5 5 5 5 '''
i=1
while i<=5:
    j=1
    while j<=5:
        if j<=i:
            print(i,end=' ')
        else:
            print(' ',end=' ')
        j=j+1
    i=i+1
    print()
'''1 
1 0 
1 0 1 
1 0 1 0 
1 0 1 0 1'''
i=1
while i<=5:
    j=1
    while j<=i:
        if j%2==0:
            print('0',end=' ')
        else:
            print('1',end=' ')
        j=j+1
    i=i+1
    print()
'''
a         
b c       
d e f     
g h i j   
k l m n o '''
i=1
k=97
while i<=5:
    j=1
    while j<=5:
        if j<=i:
            print(chr(k),end=' ')
            k+=1
        else:
            print(' ',end=' ')
        j+=1
    i+=1
    print()
'''
A         
B C       
D E F     
G H I J   
K L M N O '''
i=1
k=65
while i<=5:
    j=1
    while j<=5:
        if j<=i:
            print(chr(k),end=' ')
            k+=1
        else:
            print(' ',end=' ')
        j+=1
    i+=1
    print()
'''
#                   
$ %                 
& ' (               
) * + ,             
- . / 0 1           
2 3 4 5 6 7         
8 9 : ; < = >   '''
i=1
k=35
while i<=7:
    j=1
    while j<=7:
        if j<=i:
            print(chr(k),end=' ')
            k+=1
        else:
            print(' ',end=' ')
        j+=1
    i+=1
    print()
print()
print()
i=5
while i>=1:
    j=1
    while j<=5:
        if j>=i:
            print(i,end=' ')
        else:
            print(' ',end=' ')
        j+=1
    i-=1
    print()
print()
print()
i=1
while i>=5:
    j=5
    while j>=1:
        if j<=i:
            print(i,end=' ')
        else:
            print(' ',end=' ')
        j-=1
    i+=1
    print()
print()
print()
i=0
while i<=4:
    j=0
    k=65
    while j<=4:
        if j<=i:
            print(chr(k),end=' ')
            k+=1
        else:
            print(' ',end=' ')
        j+=1
    i+=1
    print()
print()
print()


        
                               
    
