year=int(input('Enter a year for checking the leap year or not::'))
if year%4 == 0:
    if year%100 ==0:
        if year%400 ==0:
            print('the year you have entered is a leap year:')
        else:
            print('the year {:d} is not leap year :'.format(year))
    else:
        print('the year {:d} is a leap year :'.format(year))
else:
    print('the year {:d} is not leap year :'.format(year))
