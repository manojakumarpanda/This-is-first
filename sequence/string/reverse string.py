#program to reverse the string
var1=input('Enter the string for the operation of reverse::')
var=str()
var=var1[-1:-(len(var1)+1):-1]
print(var)
st='hello'
st2=list(st)
i=0
while i<len(st):
    e=st2.pop(0)
    s=str(' '.join(st2))
    print('The string is afetr reverse="{0}"+"{1}"'.format(s,e))
    i+=1
    
