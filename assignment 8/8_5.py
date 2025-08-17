# sum of all prime number between 1 to n

def sum_prime(n):
    total = 0
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            total += i
    return total

n = 10
print(sum_prime(n))

# def prime ():
#     num = int(input("enter a number: "))
#     total = 0
#     for i in range(2,num+1):
#         if(num%i==0):
#          total +=i
        
#     print(f'sum of prime num between 1 to {num} is',total)
# prime()