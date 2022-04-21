def reverse(s): 
    return s[::-1] 
def check_palindrome(s):
    reversed_string = reverse(s)
    if s == reversed_string:
        print(s, "это полиндром")
    else:
        print(s, "это не полиндром")
 
check_palindrome("дед")
check_palindrome("дединсайд")
 
