#program for the paranthesis validation in a string man(oj]pa{da]})
st='man(oj)[]pa{}da[]{}()( jkk)'
co,cu=0,0
temp=''
for ch in range(len(st)):
        for i in range(ch,len(st)):
            if (ord(st[i]) in [41,125,93])and(ord(st[ch]) in [91,123,40]):
                flag=True
            else:
                flag=False
print(flag)           
        
        
        
