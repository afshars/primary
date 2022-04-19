# Programmer : Sara  Afshar
# Program : Calculator
# Delivery time : 1400/12/17
#------------------------------------------

class Calculator :
    def Add (a,b):
        c=a+b
        print('Addition two numbers=',c)
    def Minus (a,b):
        c=a-b
        print('Minus two numbers=',c) 
    def Multiplication (a,b):
        c=a*b
        print('Multiplication two numbers=',c) 
    def Division (a,b):
        c=a/b
        print('Division two numbers=',c) 
    def Power (a,b):
        c=a**b
        print('Power two numbers=',c)        

print("--------------------------------")        
a=float(input('plz enter num_one :')) 
b=float(input('plz enter num_two :'))
c=input('plz enter operato(+ ,-,*,/,^)  : ')

if c=='+':
    print(Calculator.Add(a, b)) 
elif c=='-':
    print(Calculator.Minus(a, b))
elif c=='*':
    print(Calculator.Multiplication(a, b))
elif c=='/':
    print(Calculator.Division(a, b))
else:
    print(Calculator.Power(a, b))
print("--------------------------------") 
