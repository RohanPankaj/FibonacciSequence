def create_sequence(a,b,c,): #make Function
      
    while a > 0: #while loop created with the conditional that it should run when a is greater than zero (should always be true with given values)
        
        c = a+b 
        print(c)
        b = c+a
        print(b)
        a = b+c
        print(a)
      

create_sequence(1,0,1) #setting values
#this does not work as it does not inclue 0 or the first 1 in the sequence
# Copywrite 2019 © Rohan S. Pankaj, All rights reserved

