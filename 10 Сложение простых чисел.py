#Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

#Найдите сумму всех простых чисел меньше двух миллионов
x=1
c=1
kvk=0
chsl=[2,3]
while c<2000001:
    x+=1
    if x%2!=0 and x%3!=0 and x%6!=0 and x%11!=0 and x%7!=0:
        chsl+=[x]
        #print(c,x)
        c+=1
for i in chsl:
    kvk+=i
print(kvk)
    
