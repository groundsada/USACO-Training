"""
ID: groundsada
LANG: PYTHON3
TASK: milk
"""
fin = open ('milk.in', 'r')
fout = open ('milk.out', 'w')

amount, farmers_number = map(int, fin.readline().split())
cost = 0
farmers =[]
for i in range(farmers_number):
    x, y  =  map(int, fin.readline().split())
    farmers.append([x,y])
farmers.sort()
for i in farmers:
    if amount > i[1]:
        amount -= i[1]
        cost += i[0] * i[1]
        if amount == 0:
            break
    else:
        cost += amount * i[0]
        break
fout.write(str(cost) + "\n")
fout.close()