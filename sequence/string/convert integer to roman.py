#program to convert the integer number to roman number
num=int(input('Enter a integer number bellow the number 100::'))
nu=num
st=''
if num>100 or num==0:
    print('You have entered a out of range number for this operation::')
def first(st,num,nu) :
    if num<=3:
        rom='I'*(num//1)
        st+=rom
        print('The roman representation of the number"{0}" is "{1}"'.format(nu,st))
    elif num==4:
              rom='IV'
              st+=rom
              print('The roman representation of the number"{0}" is "{1}"'.format(nu,st))
    elif num==5:
              rom='V'
              st+=rom
              print('The roman representation of the number"{0}" is "{1}"'.format(nu,st))
    elif num<9:
              i=num-5
              rom='V'+i*'I'
              st+=rom
              print('The roman representation of the number"{0}" is "{1}"'.format(nu,st))
    elif num==9:
              rom='IX'
              st+=rom
              print('The roman representation of the number"{0}" is "{1}"'.format(nu,st))
if num<10:
    first(st,num)
elif num>10:
    count=(num//10)
    st+=count*'X'
var=num%10
first(st,var,nu)


              
        
    
       
