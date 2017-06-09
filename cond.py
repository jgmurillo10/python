def sumarize(a,b):
    return a+b


def suma():
    i = raw_input("ingrese el primer numero a sumar")
    j = raw_input("ingrese el segundo numero a sumar")
    a = int(i)
    b = int(j)
    res = a+b
    print "Su resultado es:  %s" % (a+b)

print suma()
