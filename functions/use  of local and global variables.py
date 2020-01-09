#program for the example of local and global
a=10  #global variable can be access by any of the fuction as this is global to all
b=20   #global variable can be access by any of the fuction as this is global to all
ad=id(a)
add=id(b)
def fun1():
    '''if ad==type(a) and add==type(b):
        print('the variable here is {2}the adress are {0} and {1} local variable:'.format(type(a),ad,a))
        print('The varible here is {2} the addres are {0} and {1}local variable only:'.format(type(b),add,b))'''#this will give error as the variable with same name as the global variable name is local variable
    a=200    #This variable here is local variable only and can access by only and only by the this functio
    b=100     #the scope of this vaiable is up to this function only
    if ad==id(a) and add==id(b):
        print('the variable here is {2}the adress are {0} and {1} local variable:'.format(id(a),ad,a))
        print('The varible here is {2} the addres are {0} and {1}local variable only:'.format(id(b),add,b))
    else:
        print('The varible here is {2} and the address of the local variable is {1} and the global variable is{0}:'.format(a,id(a),ad))
        print('The varible here is {2} and the address of the local variable is {1} and the global variable is{0}:'.format(b,id(b),add))
def fun2():
    ''' a=20
        b=30
        global a,b
        a=40 b=200 This will rais a error that the varibale name of local and global variable can't use in a same function with same var name with diff function name allowed'''
    c=300#local variable
    global a,b
    a=100
    b=200
    print('The varible here is {2} and the address of the local variable is {1} and the global variable is{0}:'.format(a,id(a),c))
    print('The varible here is {2} and the address of the local variable is {1} and the global variable is{0}:'.format(b,id(b),c))
def main():
    fun1()
    e=a
    f=b
    print('The value of the global variable befor change is:{0}and after changed in the function with "keyword of global" is :{1}'.format(a,b))
    fun2()
    print('The value of the global variable befor change is:{0}and after changed in the function with "keyword of global" is :{1}'.format(e,a))
    print('The value of the global variable befor change is:{0}and after changed in the function with "keyword of global" is :{1}'.format(f,b))
main()
