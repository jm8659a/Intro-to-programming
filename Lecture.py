# countdown = 10
#
# while countdown > 0:
#     print (countdown)
#     countdown -= 1
#
# print ("Blastoff!")

#Fibonacci series
a=0
b=1
count = 2
fib = [a,b]
print ("first term = ", a)
print ("second term = ", b)

sum = 0

# while count <= 100:
#     next_term = a+b
#     fib.append(next_term)
#     a=b
#     b=next_term
#     count += 1
#
# print (fib)

while True :
    next_term = a+b
    print (count, "th term = ", next_term)
    a,b = b, next_term
    count += 1
    fib.append(next_term)
    if count == 10:
        break

print (fib)