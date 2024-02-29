def reversedNumber(number):
    
    """
    >>> reversedNumber(123)
    321
    """
    
    reversed = 0
    while number:
        reversed = 10 * reversed + number % 10
        number //= 10
    return reversed
    
    # alternative:
    # return int(str(number)[::-1])
  
def isPrime(number):
    
    """
    >>> isPrime(2)
    True
    >>> isPrime(32)
    False
    >>> isPrime(31)
    True
    """
    
    # traverse all possible divisors
    prime, divisor = True, 2
    while prime and divisor <= int(number ** .5):
        if not number % divisor:
            prime = False
        divisor += 1
        
    return prime
  
def isEmirp(number):
    
    """
    >>> isEmirp(13)
    True
    >>> isEmirp(23)
    False
    >>> isEmirp(101)
    False
    """
    
    reversed = reversedNumber(number)
    return (
        number != reversed and    # number is not a palindrome 
        isPrime(number) and       # number is prime
        isPrime(reversed)         # reversed number is prime
    )

if __name__ == '__main__':
    import doctest
    doctest.testmod()