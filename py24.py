import math

def trapez(func, a, b, N):
    h = (b - a) / N  
    result = 0.5 * (func(a) + func(b))  
    
    for i in range(1, N):
        result += func(a + i * h)  
    
    result *= h  
    return round(result, 8)  

result = trapez(math.sin, 5, 7, 100)
print(result)
