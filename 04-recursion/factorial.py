
def factorial(n):
    if n == 1 or n == 0:
        print("F: ", 1)
        return 1
    else:
        print("F: ", n)
        return factorial(n-1) * n 
    

print(factorial(5))