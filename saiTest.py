# Fibonacci Sequence Code In Python
# Copyright © 2019, Sai K Raja, All Rights Reserved

x = input("What iteration/root in the fibonacci seqeunce do you want?")

print("0")  
def fibonacci_sequence(a):  
    if a == 1:  
        return 1
    if a == 2:  
        return 1
    return fibonacci_sequence(a - 1) + fibonacci_sequence(a - 2)


for i in range(1, int(x)):
    print(fibonacci_sequence(i))


print("The last number shown is the " + str(x) + "th root of the fibonacci seqeunce.")  

input("Thank you for using my fibonacci seqeunce program.  if you would like to continue, press enter and run the program again.")


