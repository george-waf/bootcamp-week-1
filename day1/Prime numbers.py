def prime_test(num1,num2):
 for num in range(num1,num2):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)

