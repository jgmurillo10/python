bool_one = False or not True and True

bool_two = False and not True or True

bool_three = True and not (False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True)

print "False:: "
print bool_one
print "True::"
print bool_two
print "True::"
print bool_three
print "True::"
print bool_four
print "False::"
print bool_five
