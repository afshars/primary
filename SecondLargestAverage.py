# Created by : Sara  Afshar
# Program : Show the second largest grade point average 
# Delivery time : 1401/01/31
#------------------------------------------


n=int(input('plz enter num of students :'))

AVG=[]

for i in range (0,n):
    #  length's ID should be 10
    ID=input('plz enter ID of student :') 
    if len(ID) !=10:
        for i in range (0,3):
            ID=input('plz enter student`s ID  again , length`s ID should be 10 :')  
            if len(ID)==10:
                break 
    #   The average must be less than 20      
    avg =float(input('plz enter student average : '))
    if avg>20 :
        for i in range (0,3):
            avg =float(input('plz enter student`s average  again , average must be less than 20 :')) 
            if avg <=20:
                break  
    AVG.append(avg)
    
print('student average :' , AVG)
     
MAX1=max(AVG)
AVG.remove(MAX1)
MAX2=max(AVG)   
    
print('second average :' , MAX2)   



 
    