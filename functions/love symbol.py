#program to print the love symbol witg use of variable length argument
def print_value(s='*',*arg):
    for ch in range(7):
        if ch in arg:
            print('*',end=' ')
        print(end='*')
def main():
    print_value(1,2,4,5)
    print_value(1,2,3,6)
    print_value(1,5)
    print_value(1,4)
    print_value(2,4)
    print_value(2,3)

main()

    
