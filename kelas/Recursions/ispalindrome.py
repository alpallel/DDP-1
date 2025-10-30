def ispalindrome(inp):
    def palindrome(inp, n = -1):
        if n == -len(inp):
            return inp[0]
        return inp[n] + palindrome(inp, n-1)
    return palindrome(inp) == inp
    
print(ispalindrome("bammab"))