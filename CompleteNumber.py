# Created by : Sara  Afshar
# Program : Perfect Number
# Delivery time : 1401/01/31
#------------------------------------------



while True:
    for num in range (1,500):
   #num =int(input('plz enter a number :'))  
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

        sum=0
        for i in  range (len(divisors)):
            sum +=divisors[i]
            i+=1
        print('sum of divisors :',sum)

        if sum==num :
            print("The number entered is Perfect Number")
            
        answer = input('Do you want to continue? ').lower()
        if answer=='no':
            break
        num+=50