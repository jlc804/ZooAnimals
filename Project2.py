
def main():
    seats_row0 = ['Robbie', 'Brett', 'Empty', 'Empty', 'Ashlee']
    seats_row1 = ['Empty' for k in range(5)]
    seats_row2 = ['Jason', 'Brent', 'Empty', 'Empty', 'Empty']
    seats_row3 = ['Drew', 'Ryan', 'Mondaine']
    seats_row4 = ['Paul', 'James']
    seats = [seats_row0, seats_row1, seats_row2, seats_row3, seats_row4]
    seating_chart = seating_chart_class(seats)
    seating_chart.addStudent('Trey', 2,3)
    seating_chart.displaySeatingChart()
    teams = seating_chart.assignTeams()
    seating_chart.displayTeams(teams)


class seating_chart_class:
    def __init__(self, seats):
        self.seats = seats

    def addStudent(self, student_name, target_seat_row, col):
        self.seats[target_seat_row][col] = student_name

    def displaySeatingChart(self):
        for row in range(len(self.seats)):
            for element in range(len(self.seats[row])):
                print('\t' + str(self.seats[row][element]), end='\t')
            print('')


    def assignTeams(self):
        team0 = []
        team1 = []
        team2 = []
        team3 = []
        team4 = []
        teams = [team0, team1, team2, team3, team4]

        for row in self.seats:
                i = 0
                for element in row:
                    if str(element) != 'Empty':
                        teams[i].append(element)
                    i+=1
        return teams

    def displayTeams(self, teams):
        i=0
        for team in teams:
            print('Team' + str(i), end='\n')
            for members in team:
                print(members,end=' ')
            print('')
            i+=1




if __name__ == "__main__":
    main()



