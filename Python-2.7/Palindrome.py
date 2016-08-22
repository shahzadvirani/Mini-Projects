'''
Program that checks whether a string is a
palindrome or not (using recursion).
'''

def isPalindrome(x):  #function definition
    if(len(x)==0 or len(x)==1):
        return True
    else:
        return x[0]==x[-1] and isPalindrome(x[1:-1])

test_string=raw_input("Enter a string: ")

if(isPalindrome(test_string)==True):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

