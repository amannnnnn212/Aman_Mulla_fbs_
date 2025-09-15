# 2. Python Program to Concatenate Two Dictionaries Into One

di1={1:'a',2:'b'}

di2={3:'c',4:'d'}

di3={}
for i in di1:
    di3[i]= di1[i]
for i in di2:
    di3[i] = di2[i]

print("after addition :",di3)