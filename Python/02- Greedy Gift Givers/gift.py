"""
ID: groundsada
LANG: PYTHON3
TASK: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

n = int(fin.readline().encode())
friends_dict = {}
for i in range(n):
    friends_dict.update({fin.readline().strip():0})
for i in range(n):
    name = fin.readline().strip()
    amount,receivers = map(int, fin.readline().split())
    if receivers != 0:
        friends_dict[name] -= amount
        friends_dict[name] += amount % receivers
        amount = amount // receivers
    for j in range(receivers):
        friends_dict[fin.readline().strip()] += amount
for x, y in friends_dict.items() :
    fout.write(x +" "+ str(y) + "\n")
fout.close()
