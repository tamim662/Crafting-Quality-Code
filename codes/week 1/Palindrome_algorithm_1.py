def is_palindrome(s):
    
    return reverse(s)==s



def reverse(s):
    rev=''
    for char in s:
        rev=char+rev
    return rev

word=input()

print(is_palindrome(word))