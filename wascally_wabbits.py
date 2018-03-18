def fib(n):
    if n == 0:
        num = 0
    elif n == 1:
        num = 1
    else:
        num = fib(n-1) + fib(n-2)

    return(num)
with open('file') as wabbit_file:
    data_list = wabbit_file.split(' ')

n = data_list[0]
k = data_list[1]

