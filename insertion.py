def less(a,b):
    if a<b:
        return True
    else:
        return False
def change(list,i,j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
list = [3,2,1]

def sort(lists):
    i=0
    while (i<len(lists)):
        j=i
        while (j>0 and less(lists[j],lists[j-1])):
            change(lists,j,j-1)
            j-=1
        i+=1


print list
sort(list)
print list
