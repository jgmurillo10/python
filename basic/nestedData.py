students = [("Alejandro", ["CompSci", "Physics"]),
            ("Justin", ["Math", "CompSci", "Stats"]),
            ("Ed", ["CompSci", "Accounting", "Economics"]),
            ("Margot", ["InfSys", "Accounting", "Economics", "CommLaw"]),
            ("Peter", ["Sociology", "Economics", "Law", "Stats", "Music"])]
# print all students with a count of their courses.
for (name, subjects) in students:

    print(name, "takes", len(subjects), "courses")
    for sub in subjects:
        print "Those are " + sub
# Count how many students are taking CompSci
counter = 0
for (name, subjects) in students:
    for s in subjects:                 # a nested loop!
        if s == "CompSci":
            counter += 1

print("The number of students taking CompSci is", counter)
