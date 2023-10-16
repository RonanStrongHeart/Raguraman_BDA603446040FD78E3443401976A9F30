def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print('FACTORIAL OF NUMBERS')

while(True):
    Num = int(input("Enter the number to find the factorial: "))
    if(Num==-1):
        break;
    print("Factorial of",Num,"is",factorial(Num))
    print("Enter -1 to exit")

print("Sayonera") 

