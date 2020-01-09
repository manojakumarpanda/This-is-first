#introduction for the global variable
var=10
var2=323
def fun1():
    print(var,var2)
def fun2():
    global var,var2
    var='global variable '
    var2='changed'
    print(var,var2,sep='')
def main():
    fun1()
    print(var,var2)
    fun2()

main()
#Another example for the global variable
x=100
def function():
    y=200
    print('the globl variable is {0} and the local variable is {1}::'.format(x,y))
    return
def function1():
    global x
    s=20.4999
    x=int(input('Enter the value you want to chage to the global variable::'))
    print('the global variable is changed with global keyword {0} and after change{1:010.2f}::'.format(x,s))
    return
def main():
    print('This call is before the function call:',x)
    function()
    print(x)
    function1()
    print(x)
    return
main()
