s='one two three four five'
l=s.split()
li=[]
i=0
while i<len(l):
    if i%2==0:
        li.append(l[i])
    else:
        li.append(l[i][::-1])
    i=i+1              
output=' '.join(li)
print(output)                  
