def create_sequence(a,b,c):

    while a > 0: 
        c = a+b
        print(c)
        b = c+a
        print(b)
        a = b+c
        print(a)

create_sequence(1,0,0)

