import numpy

num_students = int( input( "How many students in class? " ))
seating_chart = [ None for k in range(num_students) ]
number_of_students = 10
students_in_each_row = 0
students = ['Undefined' for k in range(number_of_students)]
seat_row =[]
seat_column = []

for i in range(num_students):
    num_students_in_row = int(input('Number of students in Row {} '.format(i)))
    seating_chart[i] = num_students_in_row * ["(undefined)"]

print(seating_chart)


