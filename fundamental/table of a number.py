#program to find table of  the given number
num=int(input('Enter the number of which you want to find table :'))
fix,table,result=num,1,0
while table <=10:
    result=num*table
    print('The table of the number{0:d} in the table {1:d}*{2:d} is '.format(fix,num,table),result)
    table=table+1
#recurssion format of this program is pending

