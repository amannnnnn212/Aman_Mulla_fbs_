
def emp(edata):
    for i in range(len(edata)):
        for j in range(i,len(edata)):
            if edata[i][2] > edata[j][2] :
                edata[i],edata[j]=edata[j],edata[i]
    return edata


edata=[[101,"seema",45000],[340,"rajani",13000],[210,"tannu",14000],[320,"suresh",35000]]

res=emp(edata)

print(res)