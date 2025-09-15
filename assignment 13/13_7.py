# 7. Python Program to Remove the Given Key from a Dictionary


dict={'name':"Aman Mulla",'sal':50000,'1':"one"}

print("origional dictionary :",dict)

item=input("enter key  to remove in dictionary :")

new_dict={}

for i,j in dict.items():
    if(item != i):
        new_dict[i] = j

print("after removing key and its value in the dictionary",new_dict)