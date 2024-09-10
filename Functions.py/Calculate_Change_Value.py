change_as_tuple = (
    (3, 0, 1, 1, 0, 1),
    (4, 1, 0, 2))

def generate_bills(bills):
    # Calculate the number of each denomination
    hundreds = bills[5] * 100
    fifties = bills[4] * 50
    twenties = bills[3] * 20
    tens = bills[2] * 10
    fives = bills[1] * 5
    singles = bills[0] * 1
    total = hundreds + fifties + twenties + tens + fives + singles
    return total

def generate_coins(coins):
    quarters = coins[3] * 25
    dimes = coins[2] * 10
    nickels = coins[1] * 5
    pennies = coins[0] * 1
    total = quarters + dimes + nickels + pennies
    return total

def value_of_change(tuple):
    bills_total = generate_bills(tuple[0])
    coins_total = generate_coins(tuple[1])
    total_change = '$' + str(bills_total) + '.' + str(coins_total)
    return total_change

cash_value = value_of_change(change_as_tuple)

print("The cash value is: {}".format(cash_value))