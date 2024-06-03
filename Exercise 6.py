#You need the first term and the difference to find all the other terms of the series
#First term a1 = 1
#Difference d = 3
#nth term a_n = a1 + (n-1)*d
#n is the term number
#Use while loop to find first 10 terms
#[1, 4, 7, 10, 13, 16, 19, 22, 25]

a1 = 1
difference1 = 3
count1 = 1
list1 = []
while count1 < 10:
    next_term1 = a1 + (count1-1)*difference1
    list1.append(next_term1)
    count1 += 1
print(list1)

#Now try with different a1 and d values for example a1=1 and d=6
#[1, 7, 13, 19, 25, 31, 37]

a1 = 1
difference1 = 6
count1 = 1
list1 = []
while count1 < 10:
    next_term1 = a1 + (count1-1)*difference1
    list1.append(next_term1)
    count1 += 1
print(list1)
