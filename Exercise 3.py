#The factorial of a number is the product of all numbers up to that number.
#So, factorial 4 = 1*2*3*4
#Write a while loop to find the factorial of a number.
#Use an input statement to get the number.
number = int(input("Enter a number: "))
cursor = 1
factorial = 1
while cursor <= number:
    factorial *= cursor
    cursor += 1
print(factorial)