#Create a list of all even numbers between 0 and 100 using a while loop
list = []
number = 0
while number <= 100:
    if number%2 == 0:
        list.append(number)
    number += 1
print(list)