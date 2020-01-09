#write a program to find the area of the tringle
base=0.0
height=0.0
def area():
    global base,height
    base=float(input('Enter the base value for the tringle::'))
    height=float(input('Enter the height value fot the tringle ::'))
    return 0.5*(base*height)
def print_area():
    print('THe area of the tringel is::{:.3f}'.format(area()))
def main():
    print('The base and height of the tringle is::',base,height)
    print_area()
    print('The base and height of the tringle is::',base,height)
    return
main()

    
