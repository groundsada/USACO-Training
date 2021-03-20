"""
ID: goundsada
LANG: PYTHON3
TASK: friday
"""
fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')

n = int(fin.readline().encode())
count = [0,0,0,0,0,0,0]
daysInMonth = (31,28,31,30,31,30,31,31,30,31,30,31)
day = 0
for i in range(n):
    for j in daysInMonth:
        count[day % 7] += 1
        if (j == 28) and ((i+1900)%400==0 or ((i+1900)%100!=0 and (i+1900)%4==0)):
                day +=29
        else:
            day += j
for x in count[:len(count)-1]:
    fout.write(str(x) + " ")
fout.write(str(count[6]) + "\n")
fout.close()