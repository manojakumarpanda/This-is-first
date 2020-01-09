r=float(input("Enter the radious of the circle :"))
pi=3.147
area=pi*r**2
print('The result of the area of the circle is up to two precession:{:08.2f}'.format(area))
#we cant give any other value then space and 0 to the fill character
#this is to give the alignment to the result or the area 
print('the result of the area of the circle is up to one pression is:{:<010.3f}'.format(area))
print('the result of the area of the circle is up to one pression is:{:>010.3f}'.format(area))
print('the result of the area of the circle is up to one pression is:{:^010.3f}'.format(area))
print('the area of the circle is :{:<@10d}'.format(area))
print('the area of the circle is :{:<#10d}'.format(area))
print('the area of the circle is :{:>@10b}'.format(area))
print('the area of the circle is :{:^@10b}'.format(area))
