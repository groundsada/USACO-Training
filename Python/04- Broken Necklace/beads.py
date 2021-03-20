"""
ID: goundsada
LANG: PYTHON3
TASK: beads
"""
fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')

n = int(fin.readline())
beads = fin.readline()[:n]
max_count = 0
for i in range(n):
    beads = beads [1:]  + beads[:1] 
    start_bead =''
    end_bead = ''
    count = 0
    for x in beads:
        if start_bead == '' and x != 'w':
            start_bead = x
        if x == start_bead or x == 'w':
            count += 1
        else:
            break
    for x in beads[:count-1:-1]:
        if end_bead == '' and x != 'w':
            end_bead = x
        if x == end_bead or x == 'w':
            count += 1
        else:
            break
    max_count = max(count,max_count)
fout.write(str(max_count) + "\n")
fout.close()
