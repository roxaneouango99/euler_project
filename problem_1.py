sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum+=i
print("The sum of the multiples and 3 and 5 below 1000 is: ")
print(sum)
