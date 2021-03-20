"""
ID: groundsada
LANG: PYTHON3
TASK: namenum
"""
fin = open ('namenum.in', 'r')
fout = open ('namenum.out', 'w')
flist = open ('dict.txt', 'r')
num = fin.readline().strip()
dictList = flist.read().strip().split('\n')                
pad = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL' , 6: 'MNO' , 7: 'PRS' , 8: 'TUV' , 9: 'WXY'}
found = []
def permutation(num,item = "",letters = 0):
    if letters < len(str(num)):
        for i in pad[int(num[letters])]:
            temp = item + i
            for dictItem in dictList:
                if dictItem.startswith(temp):
                    permutation(num,temp,  letters+1)
                    break
    else:
        for dictItem in dictList:
            if dictItem == item:
                found.append(item)
        return None
permutation(num)
if not found:
    fout.write("NONE\n")
for i in found:
    fout.write(i + "\n")
fout.close()