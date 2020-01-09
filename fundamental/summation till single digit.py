#program to find the sum of the digits till the sum of the digits is a single digit
def count(num):
    i,cou=0,0
    summ=0
    while num!=0:
        i=num%10
        summ+=i
        num//=10
        cou+=1
    if summ >9:
        num=summ
        count(num)
    else:
        print('The single digit sumation of a number is:',summ)
num=int(input('Enter a number for programs:'))
count(num)        
    

    
