#program to find even or odd and also find the first number is divisiable or not by the second number
a=int(input('Enter the value for the first variable:'))
b=int(input('Enter the value for the second variable:'))
if a%2 == 0:
    print('The variabel is a even :',end=('@@'))
else:
    print('The variable is not a even or odd')
print('And the variable is :',a)
if a%b == 0:
        print("The given number i.e {0:d} is divisiable by the number {1:d}:".format(a,b))
else:
    print('The given numbr i.e {0:d} is not divisiable by the number {1:d}:'.format(a,b))
    
        

