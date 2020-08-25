def is_palindrome(s):
    n=len(s)
    return s[:n//2]==reverse(s[n-n//2:])



def reverse(s):
    rev=''
    for char in s:
        rev=char+rev
    return rev

word=input()

print(is_palindrome(word))