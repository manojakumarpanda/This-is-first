#write a program to read whmany character are repeated in the string you have entered
st1=input('Enter the string for the operation:')
st2=''
st3=''
for ch in st1: #this statement will take the character from the string 
    if ch in st2:#This statement will compare wether the ch is present in the string or not if not concatinate it if there pass
        pass
    else:
        st2=st2+ch
print(st1)
print(st2)
print()
s=[]
count=1
s=st1.split()
for c in st2:
    for i in range(len(s)):
        if c==s[i]:
            count=count+1
        print(s[i])
        print(c)
    st3+=c+str(count)
print(st3)

        
          


           
                
    
                
    
        

