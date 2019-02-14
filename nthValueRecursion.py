#This is a terrible way to find the nth value in the Fibonacci sequence as it get slowed down very fast


def fibonacci(n): 
     
    if n==0: 
        return 0
  
    elif n==1: 
        return 1
    elif n >= 2: 
        print(fibonacci(n-1)+fibonacci(n-2)) #equation generates the number in Fibonacci Sequence for the nth value
    else: 
         print("Im sorry you have entered a number that cannot be calculated.") 
    
  

  
fibonacci(int(input("What number in the Fibonacci Sequence do you want to Generate?  "))) 


