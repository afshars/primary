# Created by : Sara  Afshar
# Program : Password
# Delivery time : 1400/12/19
#------------------------------------------

# Changed password :
changed_password = input('Do you changed your password ? ').lower()

if changed_password =='yes':
    # put new password :
    while True :
        
        new_password = input('plz enter your new password :')
        repeat_new_password=input('plz enter your  the new password  again:')
        
        if new_password ==repeat_new_password:
            Mypassword=new_password
            print('your password changed successfully :)')
            break
        else :
            print('passwords do not match, plz try again :(')
else:
    Mypassword='Sara'
    
# Log in
t=1
while t<=3:
       
    print('Try', t,':')
    
    password= input('plz enter your password : ')

    if Mypassword==password:
        print('Welcome My Dear')
        break
    elif t<3:
        print('your password not True, plz try agin')
        t=t+1        
    elif t==3 :
        print('You tried  three times, plz try to another ways for get your password.')       
        break
