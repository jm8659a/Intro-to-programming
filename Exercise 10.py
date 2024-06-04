#Find the sum of the first 100 terms of the Fibonacci series.
#Start witi a = 1 and b = 1

a1=1
b1=1
count1 = 2
fib1 = [a1,b1]

sum1 = a1+b1

while count1 < 100:
    next_term1 = a1+b1
    fib1.append(next_term1)
    a1,b1 = b1, next_term1
    count1 += 1
    sum1 = sum1 + next_term1

print(fib1)
print(sum1)

#Find the first term in the series greater than 10000.

a2=1
b2=1
count2 = 2
fib2 = [a2,b2]

while True:
    next_term2 = a2+b2
    fib2.append(next_term2)
    a2,b2 = b2, next_term2
    count2 += 1
    if next_term2 > 10000:
        break

print(fib2)
print(next_term2)
