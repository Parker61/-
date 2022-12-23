
#факториал
n=3
f=1
for i in range(2,n+1):
    f*=i
print(f)



#сумма чисел числа
n=1234556565656
#print(range(n))
s=0
while n!=0:
    s+=n%10
    n=n//10
print('s',s)

s=0
n=str(1234556565656)
print(len(n))
for i in range(len(n)):
    s+=int(n)%10
    n=int(n)//10
print('s',s)



#форматирование после запятой
n=1.123456789
x=789
print(f'{n:.1f}')
print('%.3f'%n)
print(format(n,'7.4f'))

print(f'{x:8d}')
print('%8d'%x)

#НОД наименьший общий делитель
n=22
x=24
while x!=n:
    if n>x:
        n=n-x
    else:
        x=x-n
print(n)

#определение m справа число
m=3
n=123456789
count=0
while count!=m:
    posl=n%10
    count+=1
    if count==m:
        print('posl',posl)
    n=n//10

m=3
n=123456789
for i in range(m):
    posle=n%10
    n=n//10
print('posle',posle)

#определение m слева число
m=3
n=123456789
count=0
n2=n
while n2!=0:
    n2=n2//10
    count+=1
print('count',count)

for i in range(count-m+1):
    posle=n%10
    n=n//10
print('posle',posle)

#опред суммы цифр
n=123456789
s=0
while n>0:
    s+=n%10
    n=n//10
print('s',s)


#определение макс знач цифры в числе
n=39536470356
posl=n%10
max=posl
n=n//10
while n>0:
    posl=n%10
    if posl>max:
        max=posl
    n=n//10
print('posl max',max)

#определение номера макс знач цифры в числе
n=35364703569
nomer=1
nomer_max=1
posl=n%10
n=n//10
max=posl
while n>0:
    posl=n%10
    nomer+=1
    if posl>max:
        max=posl
        nomer_max=nomer
    n=n//10
print('nomer_max',nomer_max)

#проверка числа на простое
n=45
if n==2:
    print('Simple integre')
elif n%2==0:
    print('is not simple')
else:
    kol=2
    vdel=3
    while vdel*vdel<=n:
        if n%vdel==0:
            kol+=1
            break
        vdel+=2
    if kol==2:
        print('Simple integre')
    else:
        print('is not simple')

#простые числа удовлет неравенству
a=2
b=99
perv=a
if a%2==0:
    perv=a+1
if a==2:
    print(2,end=' ')
for i in range(perv,b+1,2):
    kol=2
    vdel=3
    while vdel*vdel<=i:
        if i%vdel==0:
            kol+=1
            break
        vdel+=2
    if kol==2:
        print(i,end=' ')

#какого числа выпало больше всего осадков последняя дата
lst=[2,5,7,8,8,5,9,2,4,5,6,9,5]
max=lst[0]
for i,v in enumerate(lst):
    if v>max:
        max=v
        num=i-1
print(max,i)

#поиск макс1 макс2 и номеров
import math
lst=[2,5,7,8,8,5,2,4,5,6,5]
#max1=lst[0]
max1=-math.inf
max2=-math.inf
#if max2>max1:
    #max2 = lst[0]
    #max1 = lst[1]
for i,v in enumerate(lst):
    if v>max1:
        max1=v
        num1=i+1
    else:
        max2=v
        num2=i+1
print(max1,num1,max2,num2)

# поиск макс1 макс2 и номеров
import math
lst = [1, 8, 9, 5, 8, 9, 8]
max1 = -math.inf
max2 = -math.inf
l = []
for i, v in enumerate(lst):
    if v >= max1:
        num1 = i + 1
        max1 = v
        l.append(v)
        ind = i
    if v >= max2 and v < max1:
        max2 = v
        num2 = i + 1
print('max1, num1:', max1, num1)
print('max2, num2:', max2, num2)
#вывод максимумов по порядковому номеру
for i, v in enumerate(lst):
    if v == max1:
        print(v, 'number:', i+1, end=' ')


# поиск макс1 макс2  и макс3
import math
lst = [4, 8, 9, 5, 8, 9, 8, 2, 1]
max1 = -math.inf
max2 = -math.inf
for i, v in enumerate(lst):
    if v > max1:
        max3=max2
        max2=max1
        max1 = v
    if max2 < v < max1:
        max3=max2
        max2 = v
    if max3 < v < max2:
        max3 = v
print('max1, num1:', max1)
print('max2, num2:', max2)
print('max3, num3:', max3)

# опред локальных максимумов
l=[3,7,6,2,6,4,5,9,2,6,7,8]
for i in range(len(l)-2):
    if l[i]<l[i+1]>l[i+2]:
        print(l[i+1],end=' ')

# опред наиб кол-ва подряд идущих цифр
l=[3,7,6,2,6,4,5,9,9,9,2,6,6,7,8,8,8,8]
count=1
maxl=0
for i in range(len(l)-1):
    if l[i]==l[i+1]:
        count+=1
    else:
        if maxl<count:
            maxl=count
        count=1
if maxl<count: #длина послед послед-и
    maxl=count
print(count,maxl)

# опред наиб длину монотонно возрастающего фрагмента на 1
l=[3,2,3,4,5,4,5,9,2,6,6,7,8,8,8,8]
count=1
maxl=0
for i in range(len(l)-1):
    if l[i]==(l[i+1]-1):
        count+=1
    else:
        if maxl<count:
            maxl=count
        count=1
if maxl<count: #длина послед послед-и
    maxl=count
print(count,maxl)

# опред наиб длину монотонно возрастающего фрагмента
l=[3,2,3,4,5,6,4,5,9,2,6,6,7,8,8,8,8]
count=1
maxl=0
for i in range(len(l)-1):
    if l[i]<(l[i+1]):
        count+=1
    else:
        if maxl<count:
            maxl=count
        count=1
if maxl<count: #длина послед послед-и
    maxl=count
print(count,maxl)

#########  Списки ###############
from random import randint
a=[randint(-5,5) for i in range(11)]
print(a)
l_o=[]
l_p=[]
[l_o.append(i) if i>=0 else l_p.append(i) for i in a]
print(l_o,l_p)




















