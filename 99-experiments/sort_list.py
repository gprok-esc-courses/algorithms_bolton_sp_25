import random 

Q = [25, 37, 12, 76, 33, 1, 45, 71, 16]

QS = sorted(Q)

print(Q)
print(QS)

class Test:
    def __init__(self, value, name):
        self.value = value
        self.x = random.randint(1, 100)
        self.name = name 

    def __str__(self):
        return self.name + ' ' + str(self.value) + ' ' + str(self.x)
    
tests = []
tests.append(Test(56, "A"))
tests.append(Test(78, "B"))
tests.append(Test(12, "C"))
tests.append(Test(34, "D"))
tests.append(Test(4, "E"))

tests.sort(key=lambda x: x.x)

for t in tests:
    print(t)
