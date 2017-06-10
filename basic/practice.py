def is_int(x):
    if type(x) == int:
        return True
    else:
        arr = str(x).split(".")
        if arr[1] == '0':
            return True
    return False


print is_int(2.0001)


def digit_sum(n):
    arr = str(n)
    total =0
    for i in arr:
        total+= int(i)
    return total
print digit_sum(123)

def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
print factorial(5)

def anti_vowel(string):
    anti=""
    for i in string:
        if not(i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u'):
            anti+=i
    return anti

print anti_vowel
