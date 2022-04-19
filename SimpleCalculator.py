# Created by : Sara  Afshar
# Program : simple Calculator
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
num1=float(input('plz enter num_one :')) 
num2=float(input('plz enter num_two :'))
operator=input('plz enter operator(+ ,-,*,/,^)  : ')

if operator=='+':
    Calculator.Add(num1, num2)
elif operator=='-':
    Calculator.Minus(num1, num2)
elif operator=='*':
    Calculator.Multiplication(num1, num2)
elif operator=='/':
    Calculator.Division(num1, num2)
else:
    Calculator.Power(num1, num2)
print("--------------------------------") 
