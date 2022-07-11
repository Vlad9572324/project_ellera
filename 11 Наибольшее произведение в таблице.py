c="0802229738150040007504050778521250779108"
c1="4949994017811857608717409843694804566200"
#mas1=[]
oper=[0,1,0]
oper1=[1,0,0]
io=1

#c="12347687868"
def chist(mass):
    masl=[]
    for i in range(0,len(mass),2):
        
        x=mass[i]+mass[i+1]
        if x[0]=="0":
            x=x[1]
        masl+=[int(x)]
    return masl
x=chist(c)
y=chist(c1)
for k, m in zip(oper, oper1):
    for i,l in zip(range(0,len(x)),range(0,len(x))):
        proizv=x[i]*y[l]
        print(proizv,x[i],y[l])
        if io<proizv:
            io=proizv
print(x)
print(y)
print(io)
    