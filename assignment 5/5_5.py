# 5. Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount. (Use looping to optimize
# the problem)


amount=int(input("enter amount="))

temp=amount

two_thousand= amount // 2000

amount=amount%2000

five_hundread= amount // 500

amount= amount%500

two_hundread= amount // 200

amount= amount % 200

one_hundread = amount // 100

amount= amount % 100

fifty_rupee= amount // 50

amount= amount % 50

twenty_rupee= amount // 20

amount = amount % 20

ten_rupee = amount // 10

amount = amount % 10

print(f'2000 ={two_thousand} \n500={five_hundread} \n200={two_hundread} \n100={one_hundread} \n50={fifty_rupee} \n20={twenty_rupee} \n10={ten_rupee}')
