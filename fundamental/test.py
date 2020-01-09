ch=input('Enter a character to check which type is it:')
if (ch>='A' and ch<='Z')or (ch>='a' and ch<='z'):
    print('The character you have entered is a charecter:',ch)
elif (ch <='0' and ch >='9'):
    print('The character you have entered is a digit:')
else:
    print('The character you have entered is a special character:')
