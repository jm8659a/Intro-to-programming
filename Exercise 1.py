#Use a while loop to find the sum of all digits from 1 to 100
digit = 0
sum = 0
while digit < 101:
    sum += digit
    digit += 1
print (sum)
print ("----------")
#Given a 7 digit number 6523198 - find out how many digits this number has?
num = 6523198
count = 1
while num//10 > 0:
    num = num//10
    count += 1
print(count)