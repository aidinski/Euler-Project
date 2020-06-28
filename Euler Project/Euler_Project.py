#!/usr/bin/python
sum = 0;
for i in range(1,10):
    if (i % 3 == 0 or i % 5 == 0):
        sum = i + sum;

print("The sum if number divisible by 3 and 5 under 1000 is", sum)
