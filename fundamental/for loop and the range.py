#program of the range and the for loop
ra=range(0,10,1)
for i in range(11):
    print('The values in the range i[{:d}]of for loop are:'.format(i),i,sep=',')
for r in range (10,-1,-1):
    print('The step value of the range is in r[{:d}] of the for loop are:'.format(r),r,sep=' ')
for value in ra:
    print('The values in range of value[{:d}] of the for loop are:'.format(value),value,sep=' ')
    
