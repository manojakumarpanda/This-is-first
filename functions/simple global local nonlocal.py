#simple program to the local global and nonlocal
glob=100#these ara the global variable 
gl=200
def function():
    print('The global variable in this function is:',glob,gl)
    def outer_function():
        glob=10#This is local to the outer function but act as the globl to the inner functions
        gl=20
        print('This variable here is the local variable to this outer_function only',glob,gl)
        def inner_function():
            def non_local():
                nonlocal glob,gl
                glob=5678#This statement will change the value of the outer functions variables
                gl=4567
            non_local()
            print('This is the change of the value of the variable with nonlocal variable keywords:',glob,gl)
        inner_function()
        print('This is the change of the value of the variable with nonlocal variable keywords:',glob,gl)
    outer_function()
def global_function():
    global glob,gl
    glob=1000
    gl=2000
    print('The value of the variable after the modification with use of the global keyword',glob,gl)
def main():
    function()
    print('The global variable afer all modification by the outer and the inner function:',glob,gl)
    global_function()
    print('The value of the variable after the modification with use of the global keyword',glob,gl)
    
main()
