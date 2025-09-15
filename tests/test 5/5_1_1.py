d=[2000,500,100,50,20,10,5]
amount=int(input("enter amount :"))

temp = amount
for note in d:
    if temp >= note:
        count = temp // note   
        temp = temp % note    
        print(f"{note} : {count}")
# count=0
# count1=0
# count2=0
# count3=0
# count4=0
# count5=0
# count6=0
# temp=amount
# for i in range(len(d)):
#     # if (amount %d[i] ==0) :
#     #     count+=1
#     if(d[i]==2000):
#         count+=1
#         print("2000 :",count)
#         temp-=2000
#         if(temp ==0):
#             break
#     elif(d[i]==500):
#         count1+=1
#         print("500 :",count1)
#         temp-=500
#         if(temp ==0):
#             break
#     elif(d[i]==100):
#         count2+=1
#         print("100",count2)
#         temp-=100
#         if(temp ==0):
#             break
#     elif(d[i]==50):
#         count3+=1
#         print("50",count3)
#         temp-=50
#         if(temp ==0):
#             break
#     elif(d[i]==20):
#         count4+=1
#         print("20",count4)
#         temp-=20
#         if(temp ==0):
#             break
#     elif(d[i]==10):
#         count5+=1
#         print("10 :",count5)
#         temp-=10
#         if(temp ==0):
#             break
#     elif(d[i]==5):
#         count6+=1
#         print("5 :",count6)
#         temp-=50
#         if(temp ==0):
#             break

