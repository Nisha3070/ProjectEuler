import time
start_time = time.time()

sum3 = sum(range(0, 1000, 3))
sum5 = sum(range(0, 1000, 5))
sum15 = sum(range(0, 1000, 15))

print sum3 + sum5 - sum15

print("--- %s seconds ---" % (time.time() - start_time))
