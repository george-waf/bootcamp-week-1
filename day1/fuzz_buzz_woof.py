def solution(N):
    for loop in range(1,N+1):
        if loop%3==0 and loop%5==0 and loop%7==0:
           print ("FizzBuzzWoof")
        elif loop%3==0 and loop%5==0:
           print ("FizzBuzz")
        elif loop%3==0 and loop%7==0:
           print ("FizzWoof")
        elif loop%5==0 and loop%7==0:
           print ("BuzzWoof")
        elif loop%7==0:
           print ("Woof")   
        elif loop%5==0:
           print ("Buzz")
        elif loop%3==0:
           print ("Fizz")   
        else:
           print(loop)
