"""
ID: groundsada
LANG: PYTHON3
TASK: milk2
"""

fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')

n = int(fin.readline())
times = []
for i in range(n):
    x, y = map(int, fin.readline().split())
    times.append([x,y])
times = sorted(times)
begin, end = times[0][0], times[0][1]

milk_max = end - begin
interval_max = 0

for x in times:
    x_begin ,x_end = x[0], x[1]
    if x_begin - end >= interval_max:
        interval_max = (x_begin - end)
    if begin <= x_begin and x_begin <= end:
        if end < x_end:
            end = x_end
    else:
        if end - begin > milk_max:
            milk_max = end - begin
        begin, end = x_begin, x_end

fout.write(str(milk_max) + " " + str(interval_max) + "\n")
fout.close()