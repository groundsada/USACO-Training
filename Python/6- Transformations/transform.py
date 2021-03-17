"""
ID: mhd.fir2
LANG: PYTHON3
TASK: transform
"""

fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')


before = []
after = []
n = int(fin.readline())
for i in range(n):
    before.append(fin.readline().strip())
for i in range(n):
    after.append(fin.readline().strip())

def one(before):
    result = [""] * n
    for i in range(n):
        for j in range(n):
            result[j] += before[::-1][i][j]
    return result

def two(before):
    result = before[::-1]
    for i in range(n):
        result[i] = result[i][::-1]
    return result

def three(before):
    result = [""] * n
    for i in range(n):
        for j in range(n):
            result[j] += before[i][::-1][j]
    return result

def four(before):
     result = before.copy()
     for i in range(n):
         result[i] = result[i][::-1]
     return result

def five_1st(before):
    result = four(before)
    result = one(result)
    #print(result)
    return result    

def five_2nd(before):
    result = four(before)
    result = two(result)
    #print(result)
    return result    

def five_3rd(before):
    result = four(before)
    result = three(result)
    #print(result)
    return result    

if one(before) == after:
    fout.write("1\n")
elif two(before) == after:
    fout.write("2\n")
elif three(before) == after:
    fout.write("3\n")
elif four(before) == after:
    fout.write("4\n")
elif five_1st(before) == after or five_2nd(before) == after or five_3rd(before) == after:
    fout.write("5\n")
elif before == after:
    fout.write("6\n")
else:
    fout.write("7\n")
fout.close()