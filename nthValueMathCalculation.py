def nth_Value1(n,value): #1475 is the maximum value that can be calculated 
  n = int(n)  - 1  # This step compensates for the equation being one value off when processing n
  value =  round( 1.618033988**n // 2.2 ) #equation generates the number in Fibonacci Sequence for the nth value
  print('The ' + str(n + 1) + 'th value is ' + str(value)) # tells the user what the value is at their inputed location in the fibonacci sequence


nth_Value1(input("What number in the Fibonacci Sequence do you want to Generate?  "),0)



def nth_Value(n,value): #605 is the maximun calue that can be calcumated

 '''
  n = int(n)  - 1  # This step compensates for the equation being one value off when processing n
  value = ((((1+5**(1/2))**n)-(1-5**(1/2))**n)//(2**n*(5**(1/2)))) #equation generates the number in Fibonacci Sequence for the nth value
  converts the nth value to a string for the print statement



  nth_Value(input("What number in the Fibonacci Sequence do you want to Generate?  "),0)#sets n to the user input and default sets other varibales to 0

'''

# Copyright 2019 © Rohan S. Pankaj, All rights reserved

