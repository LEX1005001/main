from random import randint


N=20
sp_1=[]

for i in range(N):
    sp_1.append(randint(-100,100))
print(sp_1)

sp_2=[] # Чётные числа
sp_3=[] # Не чётные числа
sp_4=[] # Положитедьное
sp_5=[] # Отрицательное число

sp_3=[i for i in sp_1 if i%2]
sp_2=[i for i in sp_1 if not i%2]
sp_4=[i for i in sp_1 if i>0]
sp_5=[i for i in sp_1 if i<0]

print("Чётные числа",sp_2)
print("Не чётные числа",sp_3)
print("Положительны числа",sp_4)
print("Отрицательные числа",sp_5)
