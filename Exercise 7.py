#Triangular Nnumbers
#t1 = 1
#Nth triangular number tn = (n*(n+1))/2
#Second triangular number t2 = 2*(2+1)/2 = 2*3/2 = 3
#Third triangular number t3 = 3(3+1)/2 = 3*4/2=6
#Write a while loop to find the first 10 triangular numbers.
count1 = 1
list1 = []
while count1 < 11:
    next_term1 = int(count1*(count1+1)/2) #Division returns a float
    list1.append(next_term1)
    count1 += 1
print(list1)