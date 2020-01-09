#program to find maximum of three number with argument of type required
def max_function(a,b,c=30):#this statement consist of the required with the default argumrnt which is c=30
    if a>b and a>c:
        return a
    elif b>c and b>c:
        return b
    else:
        return c
def min_function(a,b,c=29):
    if a<b and a<c:
        return a
    elif b<c and b<c:
        return b
    else:
        return c
def main():
    a=int(input('Enter the number for finding maximum::'))
    b=int(input('Enter the second number for maximum::'))
    m=max_function(a,b)
    mi=min_function(a,b)
    print('The maxmimum number in this given value is{0} and minmum value is{1}::'.format(m,mi))
main()
