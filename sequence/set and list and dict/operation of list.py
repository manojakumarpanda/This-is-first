#program to operate different function of the list push pop del
lis=[]
while True:
    print('Enter 1 for the push in to the stack ')
    print('Enter 2 for the pop of the stack')
    print('Enter 3 for the display the stack')
    print('Enter 4 for the delete the stack ')
    print('Enter 5 for exit of this operation')
    opt=int(input('Enter your choise as per the menu shown in the above::'))
    if opt==1:
        e=int(input('Enter your element to the stack::'))
        lis.append(e)
        print('The elemetn you have entered {:d} is inserted successfully:'.format(e))
        print()
    elif opt==2:
        temp=lis.pop()
        print('The element removed or poped from the stack is',temp)
        print()
    elif opt==3:
        print ('The stack is :',lis)
        print()
    elif opt==4:
        del(lis)
        lis=list()
        print()
    elif opt==5:
        break
    else:
        print('The option you have selected is not in our menue please go through menu and try again::')
        print()
        print()

        
    
    
        
        
        
