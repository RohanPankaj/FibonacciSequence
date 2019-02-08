txtN = input("Which number in the Fibonacci Sequence do you want? ")   #asks the user what nth value they want
intN = int(txtN) #makes user input an integer
def nth_Value(n, value,ntxt,valuetxt): 
    n = n - 1  # This step compensates for the equation being one value off when processing n
    value = ((((1+5**(1/2))**n)-(1-5**(1/2))**n)//(2**n*(5**(1/2)))) #equation generates the number in Fibonacci Sequence for the nth value
    ntxt = str(n+1) #converts n to a string value for the print statement
    valuetxt = str(value) #converts the nth value to a string for the print statement
    print('The ' + ntxt + 'th value is ' + valuetxt) # tells the user what the value is at their inputed location in the fibonacci sequence

nth_Value(intN,0,0,0)#sets n to the user input and default sets other varibales to 0
# Copywrite 2019 © Rohan S. Pankaj, All rights reserved