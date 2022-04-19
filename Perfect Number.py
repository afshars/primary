# Created by : Sara  Afshar
# Program : Perfect Number
# Delivery time : 1401/01/31
#------------------------------------------


print("----------------start-----------------")
while True:
   num =int(input('plz enter a number :')) 
   # divisors of  the number
   divisors =[]
   d=1
   while d<=num :
      if num % d==0:
         x= num/d
         if x!=num:
            divisors.append(int(x))
         d+=1
      else :
         d+=1

   print('divisor :',divisors)       

    # summation of divisors
   sum=0
   for i in  range (len(divisors)):
      sum +=divisors[i]
      i+=1
   print('sum of divisors :',sum)
   
    # find perfect number
   if sum==num :
      print("The number entered is Perfect Number")
    
   print("--------------------------------------")
   
   # Exit or Continue
   answer = input('Do you want to continue (y or n) ? ').lower()   
   if answer=='n':
        print("----------------finish----------------")
        break
   
