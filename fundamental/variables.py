#this is different operation of integer type 
a=10
print('the value of a is:',a)
print("The class type of a is :",type(a))
print('The address of a is :',id(a))
z=10
print('the address of the z is:',id(z))  #the address of the a and z will be same as the int is immutable and the value hold by a and z is same so the object of these variable is same
#print('\n')
b=int(19.7)
b1=int(input("Enter a valid number for operation"))
print("The value of b is:",b,b1)
print('the type of the b is:',type(b))
print('the address of the b is:',id(b),id(b1),sep='  =>')
c=int("29999")
print('The value of c:',c)
print('the type of the c is:',type(c))
value=65
print('the class type of the value is:',type(value))
print('the octal value of the vlaue is :',oct(value))
octal=oct(value)
oct1=int(octal,base=8)
print('The binary vlaue of the variable is :',oct1)
print('the address of the oct value and type of the value is:',id(octal),type(octal),sep='  =>')
hexa=hex(value)
hexa1=int(hexa,base=16)
binary=bin(value)
binary1=int(binary,base=2)
print ('The integer conversion of the hexavalue',hexa1,'\n the integer conversion of  the binary value is:',binary1)
print ('the hexadecimal value of the variable is :',hex(value))
print('the binary value of the variable is :',bin(value))
print ('The id and class type of the variable in hex and binary is:',id(hexa),type(hexa),id(binary),type(binary),sep='   =>')
b1=0b1010
b2=0b010
res=b1+b2
bin1=bin(res)
res1=int(res)
print('the value of the addition of the two binary number is :',bin1,res,res1,sep=' =>')
                                                         #this is different operation of bool type class
d=True
d1=False
print('the type of the variables are d  and d1 :',d,d1,type(d),type(d1),sep=' =>')
e=1
e1=0
e2=bool(e)
e3=bool(e1)
e4=(20>30)
print('The state of the variable is :',e4,type(e4),id(e4),sep=',')
e5=bool(59>39)
print('The state of the variable is:',e5,type(e5),id(e5),sep='>>')
print ('the values of the variable is :',e2,e3,'\n the type of the variable is:',type(e2),type(e3),sep=' =>')
e6=(True and True)
print('The state of the variable is:',e6,type(e6),id(e6),sep=' >>')
e7=(True and False)
print('The state of the variable is :',e7,type(e7),id(e7),sep=' >>')
e8=(True or True)
print('The state of the variable is :',e8,type(e8),id(e8),sep=' >>')
e9=(True or False)
print('The state of the variable is:',e9,type(e9),id(e9),sep=' >>')
                                           #this is different operation of float type class
f=12.55
f1=.555
f2=int(f1)
f3=float(100)
f4=float("100")
f5=float('10.5')
f6=float(10.44)
f7=float(0)
fi=input(print('Enter a float value for different operations'))
fii=float(fi)
print('The value and type of the fi',fi,type(fi),id(fi),'\n the value and type of the fii',fii,type(fii),id(fii),sep=' =>')
print('The different type of float intake value ',f,type(f),id(f),sep=' =>')
print('\n The different type of float intake value ',f1,type(f1),id(f1),sep=' =>')
print('\n The different type of float intake value ',f2,type(f2),id(f2),sep=' =>')
print('\n The different type of float intake value ',f3,type(f3),id(f3),sep=' =>')
print('\n The different type of float intake value ',f4,type(f4),id(f4),sep=' =>')
print('\n The different type of float intake value ',f5,type(f5),id(f5),sep=' =>')
print('\n The different type of float intake value ',f6,type(f6),id(f6),sep=' =>')
print('\n The different type of float intake value ',f7,type(f7),id(f7),sep=' =>')
                                    #this is different operation of complex type class

g=10+13j
g1=13j
g2=130
g3=complex(g2)
g4=complex(113,13)
g5=complex(10.5,15)
g6=complex(13+4j)
g7=complex(10)
g8=complex("13.+14.546j")
g9=complex("13+18j")
h=complex("100.00")
print('The different formats of the complex value ',g,type(g),id(g),sep=' =>')
print('The different formats of the complex value ',g1,type(g1),id(g1),sep=' =>')
print('The different formats of the complex value ',g2,type(g2),id(g2),sep=' =>')
print('The different formats of the complex value ',g3,type(g3),id(g3),sep=' =>')
print('The different formats of the complex value ',g4,type(g4),id(g4),sep=' =>')
print('The different formats of the complex value ',g5,type(g5),id(g5),sep=' =>')
print('The different formats of the complex value ',g6,type(g6),id(g6),sep=' =>')
print('The different formats of the complex value',g7,type(g7),id(g7),sep=' =>')
print('The different formats of the complex value ',g8,type(g8),id(g8),sep=' =>')
print('The different formats of the complex value ',g9,type(g9),id(g9),sep=' =>')
print('The different format of the complex value ',h,type(h),id(h),sep=' =>')
h1=complex(real=int(input(print('Enter the real value for the complex number'))),imag=int(input(print('Enter the immaginary value for the complex number:'))))
print('The different format of the complex value ',h1,type(h1),id(h1),sep=' =>')
real2=h1.real
img2=h1.imag
print('The real value of the complex number is :',real2,type(real2),id(real2),'\n the immaganary value of the complex number is :',img2,type(img2),id(img2),sep=' =>')
re=int(input(print("the real value of the complex number:")))
im=int(input(print('Enter the value for the immaganary of the complex number is:')))
comp=complex(re,im)
print ('The complex value with intake from user :',comp)
      



