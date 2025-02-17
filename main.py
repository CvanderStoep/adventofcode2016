def yield_numbers(n):
    for i in range(n):
        yield i

y = yield_numbers(10)
print(next(y))

for i in y:
    print(i)
