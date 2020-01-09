#programs on the sets
s={'python','java','html','css'}
s2={}#if you creat a blank set just by assigning the flower bracket then it will by default become dictionary
n=int(input('Enter the number of element you want to add in to the set::'))
for i in range(n):
    ele=input('Enter a element you want to add to the set::')
    s.add(ele)
    print('The number you have entered is successfuly added to the set',ele)
print('The set is after the addition of element is::',s)
s3=set()
while True:
    print('Enter 1) for to add element to the set')
    print('Enter 2) for to remove element to the set')
    print('Enter 3) for to display element to the set')
    print('Enter 4) for to clear element to the set')
    print('Enter 5) for to exit element to the set')
    opt=int(input('Enter your choise as per the menu shown::'))
    if opt==1:
        ele=int(input('Enter a element you want to add to the set::'))
        s3.add(ele)
        print('The number you have entered is successfuly added to the set',ele)
        print()
    elif opt==2:
        elem=int(input('Enter the  integer you want toremove from the set::'))
        #s3.remove(elem) this will generate a key value error if the element you have enter is not found in the set
        s3.discard(elem)
        #s3.remove(ele)
        print('The element removed from the set',s3.pop())
        print()
    elif opt==4:
        s3.clear()
        print()
    elif opt==3:
        print('The set is equal to::',s3)
        print()
    elif opt==5:
        print()
        break
    else:
        print('You have selcted a wrong option for the operation please check the menue and try again::')
for i in s:
    print('The element of the set are::',i)
i=iter(s)
#print(__next()__)
