def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique 
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    k, count=0, 0
    flag=False
    for i in range(10):
        k, n1=0, n
        while k<len(str(n)) and( not flag):
              if n1%10==i:
                 flag=True
              n1//=10
              k+=1
        if flag:
            count+=1
        flag=False
    return count
a=unique_digits(1231)
print(a)            
# import doctest
# doctest.testmod()
 
    
