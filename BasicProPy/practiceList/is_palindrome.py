def is_palindrome(a: list):
    a_reverse = a[::-1]
    return a == a_reverse
    
    
is_palindrome(["alpha", "beta", "gamma", "delta", "gamma", "beta", "alpha"])