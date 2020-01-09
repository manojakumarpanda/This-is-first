
#print('This is for indent error check')
               #This is for indent error check
#  print('This for space indent error check')
        #if you add a space in collumn in a statement this will give indent error
a=10
print('The value of a is:',a)
print(a)
a,b,c,d,e,f,g,h,i,j=10,20,30,40,50,60,70,80,90,100
print('The value of these variable is :',a,b,c,d,e,f,g,h,i,j)
print('The value of these variable is :',a,b,c,d,e,f,g,h,i,j,sep=',')
print('The value of these variable is :',a,b,c,d,e,f,g,h,i,j,sep='\n')
print('The value of these variable is :',a,b,c,d,e,f,g,h,i,j)
print('The value of the variable is:',a,b,c,end=',')
print('The value of the variable is :',d,e,f,end=',')
print('The value of the variable is:',g,h,i,sep=' value=',end=' mm ')
print('The value of the variable is:',j,a,c,d)
fi=open("file1","w") #single quotes cannot applicabale here
##this file operation will work only in command prompt only
print('The value of these variable is :',a,b,c,d,e,f,g,h,i,j,file=fi)
print('The value of these variable is :',a,b,c,d,e,f,g,h,i,j,sep=',',file=fi)
print('The value of these variable is :',a,b,c,d,e,f,g,h,i,j,sep='\n',file=fi)
print('The value of these variable is :',a,b,c,d,e,f,g,h,i,j,file=fi)
print('The value of the variable is:',a,b,c,end=',',file=fi)
print('The value of the variable is :',d,e,f,end=',',file=fi)
print('The value of the variable is:',g,h,i,sep=' value=',end=' mm ',file=fi)
print('The value of the variable is:',j,a,c,d,file=fi)
fi=open("fopen","w")
print('The value of a is :',10,file=fi)
      
