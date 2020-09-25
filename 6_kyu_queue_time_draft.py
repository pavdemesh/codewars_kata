def queue_time(customers, n):
    tills = dict()

    for i in range(n):
        tills["till_" + str(i)] = 0
    # print(tills)

    total_time = 0
    next_cust = 0
    cleared_customers = 0
    all_tills_empty = False

    # while cleared_customers < len(customers) and not all_tills_empty:
    while True:
        for cust in customers:
            for i in range(n):
                if tills["till_" + str(i)] == 0:
                    tills["till_" + str(i)] = cust
                    # cleared_customers += 1
                    break
        queue_moved = 0
        for i in range(n):
            if tills["till_" + str(i)] > 0:
                tills["till_" + str(i)] -= 1
                queue_moved += 1
        if queue_moved > 0:
            total_time += 1
        else:
            break

    print(tills)

    # while True:
    #     queue_moved = 0
    #     for i in range(n):
    #         if tills["till_" + str(i)] > 0:
    #             tills["till_" + str(i)] -= 1
    #             queue_moved += 1
    #     print(tills)
    #     if queue_moved > 0:
    #         total_time += 1
    #     else:
    #         break
    # print(total_time)


queue_time([10, 2, 3], 4)
# queue_time([2, 3, 10], 3)


for customer in customers:
    if served_cust < len(customers) and fill_customer(tills, customer):
        served_cust += 1

print(tills)
print(served_cust)

while move_queue(tills):
    total_time += 1
    print(tills)
print("Total time:", total_time)