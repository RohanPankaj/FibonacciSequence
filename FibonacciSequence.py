def create_sequence(a,b,c,input,test): #make Function
    while test < (input + 1): #while loop created with the conditional that it should run when a is greater than zero (should always be true with given values)
        if input == test:
                print(test)
        else:
                c = a+b 
                test = c
                b = c+a
                test = b
                a = b+c
                test = a
create_sequence(1,0,0,8,0) #setting values

# Copyrite © Rohan S. Pankaj

