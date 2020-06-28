#!/usr/bin/python
def largestpalindrome():
    largestPalindrome=0;
    buffer=0;

    for i in range(100,999):
        for j in range(100,999):
            multipication = i*j 
            multipicationString = str(multipication);
            #print(multipicationString)
            length = len(multipicationString)
            if (length == 6):
                if (multipicationString[0] == multipicationString[5]):
                    if(multipicationString[1] == multipicationString[4]):
                        if(multipicationString[2] == multipicationString[3]):
                            buffer = multipication;
            largestPalindrome = max (largestPalindrome, buffer)
            #print(largestPalindrome)
    return largestPalindrome;

998223

print(largestpalindrome());
