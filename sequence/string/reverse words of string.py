#program to reverse content of each word in a string
s=input('Enter a line of string to reverse the content of the word:')
li=[]
li=s.split()
for i in range(len(li)):
    li[i]=li[i][::-1]
    output=' '.join(li)
print('The string you have entered is {0} after the reverse word {1}:'.format(s,output))
