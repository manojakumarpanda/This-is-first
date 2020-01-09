#w.a .p to find max of three number
a=int(input('Enter first value to compairision:'))
b=int (input('Enter the second value for the compairision:'))
c=int(input('Enter the third value for the compairision:'))
if a>b and a>c:
    print('The first value i.e {:d} is the greatest between all three::'.format(a))
elif b>c:
      print('The second value i.e {:d} is the greatest between all three ::'.format(b))
else:
    print('The third value of i.e {:d} is the greatest berween all of three:;'.format(c))
if a<b and a<c :
    print('The first value i.e {:d} is the smallest between all of three number::'.format(a))
elif b<c :
    print('the second value i.e {:d} is the smallest between all of three number::'.format(b))
else:
    print('the third value i.e {:d} is the smallest amoungst all of three number::'.format(c))
    
    
