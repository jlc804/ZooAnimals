num_courses = int( input( "How many courses do you want to load? " ))
course_roster_pylist = [ None for k in range(num_courses) ]

for k in range(num_courses):
   num_students = int( input( "Number of students in course {}: ".
                              format(k) ))
   course_roster_pylist[k] = num_students * ["(undefined)"]



course_roster_pylist[1][0] = "nikola tesla"

print("\n ---- entire double-nested list and outer size --------- ")
print( course_roster_pylist )
print( "length of outer list:", len(course_roster_pylist) )
print()

print("\n ---------- nested lists and ragged row lengths ------------- ")
for k in range(num_courses):
   print( course_roster_pylist[k] )
   print( len(course_roster_pylist[k]) )