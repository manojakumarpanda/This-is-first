# W.A.P to take name roll and marks of six subject and find the result
name=input('Enter the name of the student:')
roolno=input('Enter the rool number of the student:')
odia=int(input('Enter the mark secured in odia out of 100:'))
english=int(input('Enter the mark secured in english out of 100:'))
sanskrit=int(input('Enter the mark secured in sanskrit out of 100:'))
math=int(input('Enter the mark secured in math out of 100:'))
scince=int(input('Enter the mark secured in scince out of 100:'))
social=int(input('Enter the mark secured in social out of 50:'))
histroy=int(input('Enter the mark secured in histroy out of 50:'))
total=(odia+english+sanskrit+math+scince+social+histroy)
perc=(total/600)*100
if odia > 100:
    print ('You have entered wrong mark mark canot exceed more then 100 please check again::')
elif english >100:
    print ('You have entered wrong mark mark canot exceed more then 100 please check again::')
elif sanskrit >100:
    print ('You have entered wrong mark mark canot exceed more then 100 please check again::')
elif math >100:
    print ('You have entered wrong mark mark canot exceed more then 100 please check again::')
elif scince >100:
    print ('You have entered wrong mark mark canot exceed more then 100 please check again::')
elif social >50:
    print ('You have entered wrong mark mark canot exceed more then 100 please check again::')
elif histroy >50:
    print ('You have entered wrong mark mark canot exceed more then 100 please check again::')
if odia <35:
    print('sorry sir you have failed inthe subject of odia and have secured {:d} only out of 100:'.format(odia))
elif english <35:
    print('sorry sir you have failed inthe subject of english and have secured {:d} only out of 100:'.format(english))
elif sanskrit <35:
    print('sorry sir you have failed inthe subject of english and have secured {:d} only out of 100:'.format(sanskrit))
elif math <35:
    print('sorry sir you have failed inthe subject of english and have secured {:d} only out of 100:'.format(math))
elif scince <35:
    print('sorry sir you have failed inthe subject of english and have secured {:d} only out of 100:'.format(scince))
elif social <16:
    print('sorry sir you have failed inthe subject of english and have secured {:d} only out of 50:'.format(social))
elif histroy <16:
    print('sorry sir you have failed inthe subject of english and have secured {:d} only out of 50:'.format(histroy))
if odia>35 and english>35 and math>35 and sanskrit>35 and social>16 and scince>35 and histroy>35:
    #grade=10.5
    if perc>=36 and perc<=50:
        grade='E'
        print('The name of the student is: {0} and the roll no of the student is: {1} and the grade of the student is: {2} '.format(name,roolno,grade),perc,sep='---')
    elif perc>=51 and perc<=60:
        grade='D'
        print('The name of the student is: {0} and the roll no of the student is: {1} and the grade of the student is: {2} '.format(name,roolno,grade),perc,sep='---')
    elif perc>=61 and perc<=70:
        grade='C'
        print('The name of the student is: {0} and the roll no of the student is: {1} and the grade of the student is: {2} '.format(name,roolno,grade),perc,sep='---')
    elif perc>=71 and perc<=80:
        grade='B'
        print('The name of the student is: {0} and the roll no of the student is: {1} and the grade of the student is: {2} '.format(name,roolno,grade),perc,sep='---')
    elif perc>=81 and perc<=90:
        grade='A'
        print('The name of the student is: {0} and the roll no of the student is: {1} and the grade of the student is: {2} '.format(name,roolno,grade),perc,sep='---')
    elif perc>=91 and perc<=99:
        grade='A++'
        print('The name of the student is: {0} and the roll no of the student is: {1} and the grade of the student is: {2} '.format(name,roolno,grade),perc,sep='---')
    else:
        print('The name of the student is: {0} and the roll no of the student is: {1} and sorry to inform to you that you have filed to get pass Fail:'.format(name,roolno),perc,sep='--')
print('The name of the student is:',name,'and the mark secured out of 600 is :',total,grade,sep="----")

