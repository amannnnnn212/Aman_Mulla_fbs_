# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

s_num=int(input("enter number of student = "))
total_marks=0
total_percentage=0
for i in range (0,s_num):
    Marathi=int(input("enter Marathi marks = "))
    Hindi=int(input("enter Hindi marks = "))
    English=int(input("enter English marks = "))
    Java=int(input("enter Java marks = "))
    Python=int(input("enter Python marks = "))

    total_marks= Marathi+Hindi+English+Java+Python
    percentage= (total_marks/500)*100
    
    print(f'percentage = {percentage}',end=' ')
    total_percentage=total_percentage+percentage

    # if(Marathi<=35 or Hindi<=35 or English<=35 or Java<=35 or Python<=35):
    #     print(f'fail in {Marathi}{Hindi}{English}{Java}{Python}')

average_percentage=total_percentage/s_num
# print(total_percentage)
print(f'Average percentage : {average_percentage}')