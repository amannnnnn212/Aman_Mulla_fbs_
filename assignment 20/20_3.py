# 3. Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.

def my_range(start,end,step):
        if start < end :
            if(step==0):
                step+=1
            while start < end :
                yield start
                start+=step
        else:
            if(step==0):
                step+=1
            while start > end:
                yield start
                start-=step
                if(start==end):
                     break
             

start=int(input("enter starting value :"))
end=int(input("Enter ending value :"))
step=int(input("enter step :"))

res=my_range(start,end,step)

for i in res:
    print(i)
    