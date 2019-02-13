def nth_Value(n,value,): 
       

    n = int(n)  - 1  # This step compensates for the equation being one value off when processing n
    value = ((((1+5**(1/2))**n)-(1-5**(1/2))**n)//(2**n*(5**(1/2)))) #equation generates the number in Fibonacci Sequence for the nth value
    #converts the nth value to a string for the print statement
    print('The ' + str(n + 1) + 'th value is ' + str(value)) # tells the user what the value is at their inputed location in the fibonacci sequence

nth_Value(input("Which number in the Fibonacci Sequence do you want? "),0)#sets n to the user input and default sets other varibales to 0
# Copyright 2019 © Rohan S. Pankaj, All rights reserved
'''def test(a,b,c):
    
    while a < 2:
        if: a ==0
            print(a)
            a = a + b
        else:
            print(b)
            b = a + b
            
    while a > 1:
         c = a+b 
        print(c)
        b = c+a
        print(b)
        a = b+c'''
