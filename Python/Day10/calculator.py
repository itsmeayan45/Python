def add(n1,n2):
    return n1+n2
def subs(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operations={
    "+":add,
    "-":subs,
    "*":mul,
    "/":div

}
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
for symbol in operations:
    print(symbol)
operation_symbol=input("pick an operation from the line above: ")
cal_functions=operations[operation_symbol]
answer=cal_functions(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")