a=int(input('Enter the value for a variable :'))
b=int(input('Enter the value to shift the varialble to some bit:'))
s=a
n=b
f=s<<n
z=n>>s
c=a>>b
d=a<<b
print('The original value of variable :',a)
print('The original value of variable :{:b}'.format(a))
print('The originla value of the bitwise variable is:',b,end=('@@'))
print('The originla value of the bitwise variable is:{:b}'.format(b))
print('The value of the variable after the right bitwise operation:',c,end=(' #'))
print('The value of the variable after the right bitwise operation:{:b}'.format(c))
print('the value of the variable after the left bitwise operation:',d,sep=('@#'))
print('the value of the variable after the left bitwise operation:{:b}'.format(d))
print("THe value of the variable after the right bitwise operation in reverse format:{0:d}".format(z))
print("THe value of the variable after the right bitwise operation in reverse format:{0:X}".format(z))
print("THe value of the variable after the right bitwise operation in reverse format:{0:X}".format(f))
