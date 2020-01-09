#program for the upercase function and lower case function
def uper_case(st):
    s=str()
    for ch in st:
        if ch>='a' and ch<='z':
            s=s+chr(ord(ch)-32)
        else:
            s+=ch
    return s
def lower_case(st):
    s=str()
    for ch in st:
        if ch>='A' and ch<='Z':
            s=s+chr(ord(ch)+32)
        else:
            s+=ch
    return s
def main():
    st=input('Enter the string for the operation::')
    #s=uper_case(st)
    d=lower_case(st)
    print('After the succesful conversion of the strig is:',uper_case(st))
    print('After the succesful conversion of the strig is:',d)
main()

