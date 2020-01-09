#program to input a list item and then finding all the min and max number along with the assending order and desending order
lis=list()
print(lis)
n=int(input('Enter the number of element you want to enters::'))
i=0
while i<n:
    e=int(input('Enter the element to the list ::'))
    lis.append(e)
    i+=1
print('The list after the filling the all the element:',lis)
lis.sort(reverse=True)
print(lis)

    
