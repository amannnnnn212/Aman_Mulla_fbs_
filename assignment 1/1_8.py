# 8. Write a program to convert days into years, weeks and days.

days=int(input("enter total days= "))

years=days//365

remaining_days=days%365

weeks=remaining_days//7

remaining_days=remaining_days%7

remaining_days

print(f"years={years}")
print(f"weeks={weeks}")
print(f"remaing days={remaining_days}")
