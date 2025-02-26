def fibonacci(n, memo={}) -> int:
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n == 1:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print(fibonacci(50))
