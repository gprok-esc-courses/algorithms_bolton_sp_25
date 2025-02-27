
data = [35, 12, 21, 84, 46, 11, 23, 71, 1, 31]

stop = len(data) - 1

for i in range(len(data)-1):
    for j in range(stop):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j] 
    stop -= 1

print(data)