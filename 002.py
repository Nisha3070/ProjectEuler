import time
start_time = time.time()

def fib():
    x,y = 0,1
    while True:
        yield x
        x,y = y, x+y

def even(seq):
    for number in seq:
        if not number % 2:
            yield number

def under_4_million(seq):
    for number in seq:
        if number > 4000000:
            break
        yield number   

print sum(even(under_4_million(fib())))

print("--- %s seconds ---" % (time.time() - start_time))
