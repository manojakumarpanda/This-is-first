#program to perform different set operations
j_student={'kishan','santanu','gopal','baldu'}
p_student={'manoj','hony','kishan','gopal'}
while True:
    print('Enter your option for the set ::')
    print('Enter 1) for union operation -->')
    print('Enter 2) for intersection operation -->')
    print('Enter 3) for A-B operation -->')
    print('Enter 4) for B-A operation -->')
    print('Enter 5) for exit out of the operation -->')
    opt=int(input('Enter your option out of range of menu ::'))
    if opt==1:
        output=j_student.union(p_student)
        output1=j_student|p_student
        print('The j_student set is{0} and p_student is{1} and after in union {2} and and {3}'.format(j_student,p_student,output,output1))
    elif opt==2:
        output=j_student.intersection_update(p_student)
        output2=j_student.intersection_update(p_student)
        output1=j_student&p_student
        print('The j_student set is{0} and p_student is{1} and after in intersection {2} and and {3}and and {4}'.format(j_student,p_student,output,output1,output2))
    elif opt==3:
        output=j_student.difference_update(p_student)
        output1=j_student-p_student
        print('The j_student set is{0} and p_student is{1} and after in union {2} and and {3}'.format(j_student,p_student,output,output1))
    elif opt==4:
        output=p_student.difference(j_student)
        output1=p_student-j_student
        print('The j_student set is{0} and p_student is{1} and after in union {2} and and {3}'.format(j_student,p_student,output,output1))
    elif opt==5:
        break
    else:
        print('You have entered a wrong options::')
set1={1,2,3,4,5}
set2={3,4,8,9,10}
set3={1,2,3}
b=set3.issuperset(set1)
print('This operation is for superset check for the set1={0} and set2={1} and the{2} ::'.format(set1,set3,set1.issuperset(set3)))
print('This operation is for superset check for the set1={0} and set2={1} and the {2} ::'.format(set1,set3,set3.issuperset(set1)))
print('This operation is for superset check for the set1={0} and set2={1} and the {2}::'.format(set1,set3,set3.issubset(set1)))              
print('This operation is for superset check for the set1={0} and set2={1} and the {2}::'.format(set1,set3,set1.issubset(set3)))
print('This operation is for subset check for the set1={0} and set2={1} and the result is {2}'.format(set1,set2,set1.issubset(set2)))
print('This operation is for subset check for the set1={0} and set2={1} and the result is {2}'.format(set1,set2,set2.issubset(set1)))
print('This operation is for subset check for the set1={0} and set2={1} and the result is {2}'.format(set1,set3,b))
print('This operation is for superset check for the set1={0} and set2={1} and the result is {2}'.format(set1,set2,set2.issuperset(set1),set1.issuperset(set1)))
print('This operation is for superset check for the set1={0} and set2={1} and set3={2} the update of the '.format(set1,set2,set3),set1.update(set2))
print('This operation is for superset check for the set1={0} and set2={1} and set3={2} the update of the '.format(set1,set2,set3),set1.isdisjoint(set2))
print('This operation is for superset check for the set1={0} and set2={1} and set3={2} the update of the '.format(set1,set2,set3),set1.isdisjoint(set3))
print('This operation is for superset check for the set1={0} and set2={1} and set3={2} the update of the '.format(set1,set2,set3),set1.(set2))


