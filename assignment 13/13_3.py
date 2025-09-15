# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

dict={"1":"first","2":"second","3":"third","4":"fourth"}

print("origional dictionary :",dict)

key=input("\nwhich key you want to check select here :")

for i in dict:
    if key in dict:
        print(f'\n{key} key is exist in dictionary')
        break
    else:
        print(f'\n{key} key is does not exist in dictionary')
        break