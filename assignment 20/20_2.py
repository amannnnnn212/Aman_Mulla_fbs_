# 2. Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.

def palindrome():

    i = 1
    while True:
        temp = i
        total = 0

        while temp > 0:
            digit = temp % 10
            total = total * 10 + digit
            temp = temp // 10

        if total == i:
            yield i
        i += 1

res=palindrome()

for i in range(1,121+1):
    print(next(res))



