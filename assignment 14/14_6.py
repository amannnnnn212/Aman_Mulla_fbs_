# 6. Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.

# (1*2=2), (1*3=3), (1*4=4), (2*3=6), (2*4=8), (3*4=12)

def product_maxx(li,li2):
    pairs=[]
    for i in range(len(li)):
        for j in range(i,len(li)-1):
            li2.append(li[i]*li[j+1])
            pairs.append((li[i], li[j+1]))
        
    
    max=li2[0]
    max_pair=pairs
    for i in range(len(li2)):
        if li2[i] > max :
            max=li2[i]
            max_pair=pairs[i]
    print(f'maximum pair :{max_pair}')
    return max


li=[100,1,2,3,-99,-99,-100]
li2=[]

res=product_maxx(li,li2)

print(f'the maximum calculation of pair of two number : {res}')