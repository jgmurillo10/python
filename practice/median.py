import math
def median(numbers):
    numbers.sort()
    print numbers
    if len(numbers)%2==0:
        print numbers
        print len(numbers)
        print len(numbers)/2.0
        num = numbers[int(math.ceil(len(numbers)/2.0))-1]
        den = numbers[int(math.floor(len(numbers)/2.0))]
        print num,den
        return (num + den)/(2.0)
    else:
        return numbers[len(numbers)/2]


print median([1,2,1,2])
