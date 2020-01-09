ch=input('Enter a character to check which type is it:')
if (ch>='A' and ch<='Z')or (ch>='a' and ch<='z'):
    print('The character you have entered is a charecter:',ch)
elif (ch<='0' and ch>='9'):
    print('The character you have entered is a digit:')
else:
    print('The character you have entered is a special character:')
def conv(ch):
    if (ch>='A' and ch<='Z'):
        c=ord(ch)+32
        co=chr(c)
        print('The character you have entred is {0} and after conversion {1} is:'.format(c,co),ch)
    elif (ch>='a' and ch<='z'):
        c=ord(ch)-32
        co=chr(c)
        print('The character you have entred is {0} and after conversion {1} is:'.format(c,co),ch)
    else:
        print('The character is illigal to convert :')
conv(ch)
