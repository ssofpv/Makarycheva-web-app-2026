cube = lambda x: x ** 3

def fibonacci(n):
    # return a list of fibonacci numbers
    fib_list = [0, 1]
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
        
    return fib_list

if __name__ == '__main__':
    try:
        n = int(input())
        print(list(map(cube, fibonacci(n))))
    except (ValueError, IndexError):
        pass