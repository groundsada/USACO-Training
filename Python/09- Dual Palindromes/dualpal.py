"""
ID: groundsada
LANG: PYTHON3
TASK: dualpal
"""
fin = open ('dualpal.in', 'r')
fout = open ('dualpal.out', 'w')

def decToBase(num,base):
    result = ""
    x = num
    while x > 1:
        remainder = x % base
        if remainder < 10:
            result += str(remainder)
        else:
            result += chr(64 + remainder - 9)
        x = x // base
    if not result or x == 1:
        result += str(x)
    return result[::-1]

n, s = map(int, fin.readline().split())
count = 0
while (count < n):
    s += 1
    dual = 0
    for i in range(2,11):
        if decToBase(s, i) == decToBase(s, i)[::-1]:
            dual +=1
            if dual == 2:
                fout.write(str(s) + "\n")
                count += 1
                break
fout.close()