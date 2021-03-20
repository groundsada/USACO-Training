"""
ID: goundsada
LANG: PYTHON3
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
group = fin.readline().strip()
comet = fin.readline().strip()
x = 1
y = 1
for i in group:
    x *= (ord(i)-64)
for j in comet:
    y*= (ord(j)-64)
if (x%47 == y%47):
    fout.write("GO\n")
else:
    fout.write("STAY\n")
fout.close()