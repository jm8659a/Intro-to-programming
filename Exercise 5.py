a=1
b=1
count = 2
fib = [a,b]

sum1 = a+b

while count < 5:
    next_term = a+b
    fib.append(next_term)
    a,b = b, next_term
    count += 1
    sum1 = sum1 + next_term

print(fib)
print(sum1)
print(sum(fib))