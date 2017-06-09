def less(a,b):
    return a<b

def change(list,i,j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
def sort(list):
    i=0
    while(i<len(list)):
        j=i
        min=i
        while(j< len(list)):
            if less(list[j], list[min]):
                min=j
            j+=1
        change(list,i,min)

        i+=1

l = [3,2,1]
print l
sort(l)
print l
