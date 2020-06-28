#!/usr/bin/python
def smallestMultiple(n):
    initialNumber = n;
    counter = 1;
    while True:
        counter = 0;
        for i in range(3,n+1):
            if (initialNumber % i == 0):
                #print(initialNumber , "is divisible by ", i)
                counter = counter + 1;
            else:
                break;
        initialNumber=initialNumber+1;
        #print(initialNumber);
        

        if(counter == n-4 or counter == n-6 or counter == n-8):
            print(initialNumber-1);
        elif (counter == n-2):
            print("Smallest multiple of", n, "is ", initialNumber-1);
            break;



 

smallestMultiple(20)

