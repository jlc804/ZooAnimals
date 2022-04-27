
def main():
    seats_row0 = ['Empty' for k in range(5)]
    seats_row1 = ['Empty' for k in range(5)]
    seats_row2 = ['Empty' for k in range(5)]
    seats_row3 = ['Empty' for k in range(3)]
    seats_row4 = ['Empty' for k in range(2)]
    seats = [seats_row0, seats_row1, seats_row2, seats_row3, seats_row4]
    #test = [[seat0],[seat2]]
    seating_chart = seating_chart_class(seats)
    seating_chart.addStudent('Trey', 4,0)
    seating_chart.displaySeatingChart()






class seating_chart_class:
    def __init__(self, seats):
        self.num = 20
        self.name = 'Student'
        self.seats = seats

    def addStudent(self, student_name, target_seat_row, col):
        self.seats[target_seat_row][col] = student_name

    def displaySeatingChart(self):
        for row in range(len(self.seats)):
            # print('Row: '+str(row), end='')
            for element in range(len(self.seats[row])):
                print('\t' + str(self.seats[row][element]), end='')
            print('')

    def assignTeams(selfs):





















if __name__ == "__main__":
    main()



