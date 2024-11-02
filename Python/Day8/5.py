def prime_checker(num):
    count=0
    for i in range(2,num-1):
        if(num%i==0):
            count+=1
    if(count==0):
        return True
    else:
        return False
num=int(input("Enter a number: "))
print(prime_checker(num))