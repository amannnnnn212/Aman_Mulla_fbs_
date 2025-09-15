
def count(li):
    dict={}

    for i in li:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict

li=[1,2,4,1,2,3,6,7,1,2,4]

res=count(li)

print(res)