
def hanoi(n, current, destination, aux):
    if n > 0:
        hanoi(n-1, current, aux, destination)
        print("move", n, current, destination)
        hanoi(n-1, aux, destination, current)


hanoi(3, "A", "C", "B")