
def fibonnacci(n):
    if n == 0 or n == 1:
        return n 
    else: 
        return fibonnacci(n-1) + fibonnacci(n-2)
    

print(fibonnacci(9))