def test(a,b,n,c):
    if n == 1:
        print(a)
    elif n >= 2:
        print(a, b)
        for n in range(2,n): 
            c=a+b
            print(c)
            a=b
            b=c
    else: 
        print("Im sorry you have entered a number that cannot be calculated.")

test(0,1,int(input("What number in the Fibonacci Sequence do you want to Generate?  ")), 0)