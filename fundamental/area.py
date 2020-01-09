#program to find the area of different geomatric structre
def circle(a,b):
    p='3.147'
    pi=int(p)
    r=float(input('Enter the value of radious of the circle:'))
    area=p*(r**2)
    print('The area of the circle is ::',area)
    return
def square():
    a=float(input('Enter the side of the square:::'))
    area=a**2
    print('The area of the square is ::',area)
    return
def rectangle():
    a=float(input('Enter one side of the rectangle for calculate area:'))
    b=float(input('Enter another side of the rectangel for calculate area::'))
    area=a*b
    print('The area of the rectangle is::',area)
    return
def tringle():
    a,b,c=input('Enter the value of the Three  side of the tringle with space between values::').split(' ')
    if a==b and a==c and b==c :
        d=0.4330127018992219*(a**2)
        print('the area of the tringle is ::',d)
    else a not=b and b not= c and c not= a:
        s=0.5* (a+b+c)
        d=s*(s-a)(s-b)(s-c)
        print('the area of the tringle is:',d)

    
       
        
    
    
        
    
