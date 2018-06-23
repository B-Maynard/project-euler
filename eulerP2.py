def fib(maxIndex):
    first = 1
    second = 1
    hold = 0
    sum = 0

    while second < maxIndex:
        if second % 2 == 0:
            sum += second
        hold = first + second
        first = second
        second = hold

    print(sum)

fib(4000000)
