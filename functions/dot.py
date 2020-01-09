import re
st='aaa abc acd a'
result=re.search(r'.',st)
print('The standard outpur form the "." character function in regular expression is',result)
print('The positional and the value of the . character ',result.group(),result.span())
    
 
