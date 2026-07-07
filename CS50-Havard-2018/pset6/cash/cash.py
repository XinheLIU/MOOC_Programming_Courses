import cs50

while True:
    print("Change owed: ")
    amount = cs50.get_float()
    if amount >= 0:
        break
# num is the number of coins
num = 0
cents = int(round(amount * 100))
coins = [25, 10, 5, 1]
for coin in coins:
    num += cents // coin
    cents %= coin
print("{}".format(num))