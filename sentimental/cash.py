from math import trunc
bill = float(input("what is your bill?"))
cents = bill * 100
quarters, dimes, nickels = 0, 0, 0
while (cents >= 25):
    quarters = trunc(cents / 25)
    cents = cents % 25
while(cents >= 10):
    dimes = trunc(cents / 10)
    cents = cents % 10
while(cents >= 5):
    nickels = trunc(cents / 5)
    cents = trunc(cents % 5)
coins = round(quarters + dimes + nickels + cents)
print(coins)
# print(coins, quarters, dimes, nickels, cents)