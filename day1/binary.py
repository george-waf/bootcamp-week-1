def binary_converter(n):
    if(n==0):
        return "0"
    elif(n<0):
        return "Enter a positive integer"
    else:
        ans=""
        while(n>0):
            v=n%2
            ans=str(v)+ans
            n=n//2
        return ans  
