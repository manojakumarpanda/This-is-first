#program to find the two string are angram or not in army op mary
st=input('Enter the first string for angram check or not:')
st1=input('Enter the second string for angram check true or fale:')
flag=True
if len(st)==len(st1):
    for i in st:
        if i in st1:
            continue
        else:
            flag=False
            print('The first string you have entered is {0} and the second string is {1}'.format(st,st1))
            print('The output of the angram word or not is:',flag)
print('The output of the angram test is :',flag)
