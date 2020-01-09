#program to calcualtor function with the nested function
num1=int(input('Enter the first value for the operation ::'))
num2=int(input('Enter the second value for the operations::'))
result=0
def calculator():
    def addition():
        global result
        result=num1+num2
        print('The addition of the number is {0}+{1}='.format(num1,num2),result)
        return
    def substraction():
        global result
        result=num1-num2
        print('The substraction of the number is {0}-{1}='.format(num1,num2),result)
        return
    def multiplication():
        global result
        result=num1*num2
        print('The substraction of the number is {0}*{1}='.format(num1,num2),result)
        return
    def division():
        global result
        result=num1//num2
        print('The substraction of the number is {0}//{1}='.format(num1,num2),result)
        return
    def modular():
        global result
        result=num1%num2
        print('The substraction of the number is {0}%{1}='.format(num1,num2),result)
        return
    while True:
        print('1) for the addition operation:')
        print('2) for the substraction operation:')
        print('3) for the multiplication operation:')
        print('4) for the divisiion operation:')
        print('5) for the modular division operation:')
        print('6) for exit function')
        op=int(input('Enter your option for the operation::'))
        if op==1:
            addition()
        elif op==2:
            substraction()
        elif op==3:
            multiplication()
        elif op==4:
            division()
        elif op==5:
            modular()
        else:
            break

def main():
    calculator()

main()

    
