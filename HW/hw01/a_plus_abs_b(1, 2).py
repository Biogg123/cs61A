

def a_plus_abs_b(a, b):
    if b < 0:
        return a - b
    else:
        return a + b
    
A= a_plus_abs_b(1, 2)
print(A)