def ispalindrome(inp, n=-1):
    if n == -1 * (len(inp)):
        return inp[0]
    hasil = (inp[n] + ispalindrome(inp,n-1))
    if hasil == len(inp):
        return str(hasil) == inp
    
print(ispalindrome("bambang"))