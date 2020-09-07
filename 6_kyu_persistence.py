def persistence(n):
    # Create counter and set it initially to 0
    # Create copy of n
    counter = 0
    tmp = n

    # Repeat while initial number and subsequent products are greater than 9
    while tmp > 9:
        res = 1
        # Convert number to string and iterate over individual digits
        # Multiply digits (strings converted to ints)
        for dig in str(tmp):
            res *= int(dig)
        # Increase counter by 1
        counter += 1
        # Update the number / subsequent products
        tmp = res
    return counter


print(persistence(28))
