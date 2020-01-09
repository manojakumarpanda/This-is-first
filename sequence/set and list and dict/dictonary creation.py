#program to the dictonary creation in different types 
a=dict(name='manoja kumar panda',roll='12ec27',course='python',fee=3000,address='Tara devi temple street lanjipalli ,berhampur')
b={'name':'manoja kumar panda','roll':'12ec27','course':'python','fee':3000,'address':'Tara devi temple street lanjipalli ,berhampur'}
c=dict(zip(['one','two',3],[1,2,'three']))
d=dict([('one',1),('two',2),(3,'three')])
e=dict({'one':1,'two':2,3:'three'})
print(a)
print(b)
print(c)
print(d)
print(e)
for i,j in a.items():
    print('key:',i,'value:',j)
print(type(a.items()))

