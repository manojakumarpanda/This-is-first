#Program to count number of vowel in the string
def count_vowel(st):
    count,count1=0,0
    for ch in st:
        if ch in 'aeiouAEIOU':
            count+=1
        else:
            count1+=1
    return count,count1
def main():
    s=input('Enter the string for the operation:')
    print('The string you have entred is {0} and the vowel and non vowel is ::'.format(s),count_vowel(s))
main()
