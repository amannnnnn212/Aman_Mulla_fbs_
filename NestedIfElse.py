# nested if else

num=int(input("enter number="))


if(num>0):
   if(num>50):
      if(num>100):
         if(num>150):
            if(num>200):
               print(f'{num} is greater than 200')
            else:
               print(f'{num} is greater than 150 but less than 200')
         else:
            print(f'{num} is greater than 100 but less than 150')
      else:
         print(f'{num} is greater than 50 but less than 100')
   else:
     print(f'{num} is greate than zero but less than 50') 
else:
   print(f'{num} is less than zero or 0' )  
