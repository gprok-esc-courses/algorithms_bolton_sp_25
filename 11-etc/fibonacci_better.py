mem = {}

def fibonacci(n): 
    if n in mem:
        print("mem:", n)
        return mem[n]
    if n == 0 or n == 1:
        return n 
    f = fibonacci(n - 1) + fibonacci(n - 2)
    if n not in mem:
        mem[n] = f
    return f
    

print(fibonacci(6))