# 7. Use a nested list comprehension to find all of the numbers from
# 1–1000 that are divisible by any single digit. 
# Nested list comprehension

numbers = [num  for num in range(1, 1001) if (num % 1==0  or num % 2==0 or num % 3==0 or num % 4==0 or num % 5==0 or num % 6==0 or num % 7==0 or num % 8==0 or num % 9 == 0 )]

# numbers = [num for num in range(1, 1001)  if (num % d for d in range(1,10))]

print(numbers)


