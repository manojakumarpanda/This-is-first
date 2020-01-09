uname=input("Enter the username::")
passw=input('Enter the password::')
print('the username and password are respectfully :',uname,passw,sep='*****')
x,y=input('Enter two number for input function with space included:').split(' ')
print('the value of x and y is:',x,y,type(x),type(y),id(x),id(y))
m,n=input('Enter two integer number for arrithmatic opeation with space included:').split(' ')
#a,b=int(m,n)
'''this type of integer converssion is
illegal at a time two string can't pass as argument for int class'''
#these are the different rype of arrithmatic operator available in python
a=int(m)
b=int(n)
summ=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b
flordiv=a//b
exp=a**b
print('the first unchanged exponentional of two number is :',exp,type(exp),id(exp),sep='>>')
print('the value and type of the variable a is :',a,type(a),id(a),'the type and value of b is:',b,type(b),id(b),sep=' ')
print('the addition of two number is:',summ,id(summ),sep='  ')
print('the substraction of two number is :',sub,id(sub),sep=' ')
print('the multification of two number is:',mul,id(mul),sep=' ')
print('the division of two number is :',div,id(div),sep=' ')
print('the modular division of two number is:',mod,id(mod),sep=' ')
print('the flordivision of two number is :',flordiv)
e1=a//100
e2=b//100
exp=a**b
print('the exponentional of two number is:',exp,id(exp),sep=' ' )
a,b,c,d=input('enter four number for input operations with space berween number:').split(' ')
print('the different variable that inputed from keyboard:',a,type(a),b,type(b),c,type(c),d,type(d),sep=' >>>')

