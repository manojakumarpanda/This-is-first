#program to print all the alphabet and the special character and digits
a=0
while a<=64:
    print('The equvelent special charecter of the integer==>{:d} is :'.format(a),chr(a),sep=',')
    a+=1
while a>=65 and a<=96:
    print('The equvelent character alphabet of the integer==.{:d}is :'.format(a),chr(a),sep=',')
    a+=1
while a>=97 and a<=122:
    print('The equevelent charecter alphabet of the integer==>{:d} is :'.format(a),chr(a),sep=',')
    a+=1
