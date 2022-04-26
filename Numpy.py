import numpy as np

MIN_COURSES = 1
MAX_COURSES = 10
MIN_STUDS = 1
MAX_STUDS = 20

# part 1: get the number of courses
while True:
   try:
      num_courses = int( input(
         "How many courses do you want to load (int {}-{})? ".
                             format(MIN_COURSES, MAX_COURSES)) )
      if (MIN_COURSES <= num_courses <= MAX_COURSES):
         break
   except (ValueError, TypeError) as err:
      pass

# an array of size num_courses, where each element is an array
course_roster_numpy = np.empty( (num_courses), dtype = np.ndarray )

# part 2: get the size of each course
for k in range(num_courses):
   while True:
      try:
         num_students = int( input( "Number of students in course {} ({}-{}): ".
               format(k, MIN_STUDS, MAX_STUDS) ))
         if (MIN_STUDS <= num_students <= MAX_STUDS):
            break
      except (IndexError, ValueError, TypeError) as err:
         pass
   course_roster_numpy[k] = np.array(
      (num_students * ["(undefined)"]),
      dtype = object)

# part 3: fill rosters with distinct names
for k_crs in range(num_courses):
   for k_std in range(course_roster_numpy[k_crs].size):
      course_roster_numpy[k_crs][k_std] \
         = "lily_" + str(k_std)  + " obrien_" + str(k_crs)

# part 4: show the rosters

print("\n --------------- nested arrays -------------------- ")
for k in range(num_courses):
   print( "Course #{} --------\n{}".format(k, course_roster_numpy[k]) )
   print()

