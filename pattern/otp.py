#program to generate  a 4 digit otp for the operation
from random import randint
randint(0,9)
def generate_otp():
    rand=randint(0,9)
    return rand
i=0
while i<=4:
    generate_otp()
    i+=1
    
