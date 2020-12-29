import random as rand

listat, listres, pivot = [5,2,9,7,4,78,94,2346,8774,1,65], [], 0
"""def triSelect(listat,listres):
    min = 10000
    if len(listat)>0 :
        for i in range(len(listat)):
            if listat[i] <= min:
                min = listat[i]

        listres.append(min)
        listat.remove(min)

        return triSelect(listat,listres)

    else : return listres

print(triSelect(listat,listres))"""

def fusion(l1,l2):
    l3 = []
    id = 0
    for row in l1:
        while len(l2)>0 :
            if l2[0] < row :
                l3.append(l2[0])
                l2.pop(0)
        else : l3.append(row)
    return l3
            
"""def fusionsort(listat):
    if len(listat)>0:
        l1t, l2t = [],[]
        l1 = listat[:len(listat)//2]
        l2 = listat[len(listat)//2:]

        l1t = fusionsort(l1)
        l2t = fusionsort(l2)

        return fusion(l1,l2)
    else: return listat"""



print(fusion([2,4,6,8],[1,5,7,9]))

#print(fusionsort(listat))

