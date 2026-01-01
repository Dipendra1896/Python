def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n+1):
        product *= i
    return product
for n in range(1,10):
    print(n, factorial_function(n))
 
#Outputs:
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120
# 6 720
# 7 5040
# 8 40320
# 9 362880