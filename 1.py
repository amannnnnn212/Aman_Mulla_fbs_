# 1. Convert the time entered in hh,min and sec into seconds.

second=int(input("enter seconds ="))

temp= second

hour= second // 3600

remaining_second= second % 3600

minutes= remaining_second // 60

remaining_second = remaining_second % 60

print(f'hours= {hour} hour \nminutes= {minutes} minutes \nremaing second = {remaining_second} second')