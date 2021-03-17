"""
ID: groundsada
LANG: PYTHON3
TASK: palsquare
"""
fin = open ('palsquare.in', 'r')
fout = open ('palsquare.out', 'w')

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

base = int(fin.readline().strip())
for i in range(1,301):
    convert = decToBase(i,base)
    convert_square = decToBase((i*i), base)
    if convert_square == convert_square[::-1]:
        fout.write(convert + " " + convert_square + "\n")
fout.close()