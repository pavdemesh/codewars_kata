def queue_time(customers, n):
    tills = dict()

    for i in range(n):
        tills[i] = 0
    # print(tills)

    total_time = 0
    served_cust = 0
    all_tills_empty = False
    all_customers_served = False
    x = True

    while x:
        # print("served cust at the begin of iteration is:", served_cust)
        if served_cust < len(customers):
            for cust in customers[served_cust:]:
                # print("Current customer is: ", cust)
                if fill_till(tills, cust):
                    served_cust += 1
                    # print("Added one customer, served_cust is now:", served_cust)
            # print("after filling the served_cust is:", served_cust)
        else:
            all_customers_served = True
            # print("all customers served")
            # print("counter of served-cust is now:", served_cust)

        if move_queue(tills):
            total_time += 1
        elif all_customers_served:
            all_tills_empty = True
        x = not(all_customers_served and all_tills_empty)
        # print(x)
    return total_time


def fill_till(tmp_tills, tmp_customer):
    till_filled = False
    for i in range(len(tmp_tills)):
        if tmp_tills[i] == 0:
            tmp_tills[i] = tmp_customer
            till_filled = True
            break
    return till_filled


def move_queue(tmp_tills):
    queue_moved = False
    for i in range(len(tmp_tills)):
        if tmp_tills[i] > 0:
            tmp_tills[i] -= 1
            queue_moved = True
    return queue_moved


# print(queue_time([2, 3, 10], 2))
# print(queue_time([1, 2, 3, 4, 5], 1))
print(queue_time([2, 2, 5, 10, 8], 3))
