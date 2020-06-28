#!/usr/bin/python
def sumOfSquare(n):
    sumOfSquare = 0;
    for i in range (1,n+1):
        sumOfSquare = i**2 + sumOfSquare;
    return sumOfSquare;


def squareOfSum(n):
    sum = 0;
    for i in range (1,n+1):
        sum = i + sum;

    return sum**2;



def squareOfSumDiffSumOfSquare(n):
    sumOfSquare = 0;
    sum = 0;
    for i in range (1,n+1):
        sumOfSquare = i**2 + sumOfSquare;
        sum = i + sum;

    return ((sum**2)-sumOfSquare);


def enhancedSum(n):
    sum = ((n*(n+1))/2);
    sumSquare = ((2*n) +1)*(n+1)*n/6;
    return (sum**2 - sumSquare);


print(squareOfSum (100)-sumOfSquare (100));
print(squareOfSumDiffSumOfSquare(100));
print(enhancedSum(100));