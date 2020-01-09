#function with default argument in function
def fun(a,b,c,d=30,e=20):
            print('The value of the variablea are{0},{1},{2},{3},{4} and the sum of the numbers is ::{5} and multiplication is ::{6}'.format(a,b,c,d,e,a+b+c+d+e,a*b*c*d*e))
def draw_line(s='@',l=30):
    for ch in range(l):
        print(s,end=' ')
    print()
def main():
    a=int(input('Enter the number:'))
    p=int(input('Enter the number:'))
    r=int(input('Enter the number:'))
    fun(a,p,r)
    fun(a,p,r,d=2,e=3)
    fun(a,p,r,d=3)
    fun(a,p,r,e=3)
    draw_line(s='*')
    draw_line(s='#',l=20)
    draw_line(l=10)
main()
