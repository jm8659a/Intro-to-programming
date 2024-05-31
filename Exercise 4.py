# Use the while loop to find the smallest number that is divisible by all integers
# from 1 to 9
# The answer is 2520.

# Any number that is divisible by 8 is also divisible by 4 and 2.
# Any number that is divisible by 6 or 9 is also divisible by 3.
# Therefore, the code does not need to explicitly check if number is divisible by 2, 3, or 4.
number = 1
while number%5 != 0 or number%6 != 0 or number%7 != 0 or number%8 != 0 or number%9 != 0:
    number += 1
print(number)