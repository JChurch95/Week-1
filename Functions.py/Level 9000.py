def generate_bills(bills):
    # Convert string input to integer, because maths
    bills = int(bills)
    # Calculate the number of each denomination
    # Order matters here!
    # Starting with singles will spit out a stack of $1 bills!
    hundreds = bills // 100 # divide the bills by hundreds
    bills %= 100            # update the bills to no longer count the hundreds
    fifties = bills // 50   # divide by fifties
    bills %= 50             # update the bills to no longer count the fifties
    twenties = bills // 20  # divide by twenties
    bills %= 20             # update the bills to no longer count the twenties
    tens = bills // 10      # divide by tens
    bills %= 10             # update the bills to no longer count the tens
    fives = bills // 5      # divide by fives
    bills %= 5              # update the bills to no longer count the fives
    singles = bills // 1    # finish up with the singles
    return (singles, fives, tens, twenties, fifties, hundreds)

def generate_coins(coins):
    coins = int(coins)
    quarters = coins // 25
    coins %= 25
    dimes = coins // 10
    coins %= 10
    nickels = coins // 5
    coins %= 5
    pennies = coins // 1
    return (pennies, nickels, dimes, quarters)

def make_change(total, payment):
    difference = round(payment - total, 2)
    difference_string = str(difference)
    parts = difference_string.split('.')
    bills_part = parts[0]
    coins_part = parts[1]

    bills_tuple = generate_bills(bills_part)
    coins_tuple = generate_coins(coins_part)
    return (bills_tuple, coins_tuple)

change_as_tuple = make_change(201.61, 300)

print("Change as tuple is: {}".format(change_as_tuple))