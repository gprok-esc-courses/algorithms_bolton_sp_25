coins = [2, 1, 0.5, 0.2, 0.1]

payment = float(input("Payment: "))
inserted = int(input("Inserted: "))

change = []
remaining = inserted - payment

for coin in coins:
    while remaining >= coin:
        change.append(coin)
        remaining -= coin 

print(change)



