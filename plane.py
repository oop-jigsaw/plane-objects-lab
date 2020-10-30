# create the plane class here

import datetime
class Plane:
    def __init__(self, seats_per_row, year, number_of_rows = 20):
        self.seats_per_row = seats_per_row
        self.number_of_rows = number_of_rows
        self.year = year
        
    def age(self):
        now = datetime.datetime.now()
        current_year = now.year
        return current_year - self.year
    
    def total_seats(self):
        return self.seats_per_row*self.number_of_rows


boeing = Plane(seats_per_row=10, number_of_rows=30, year = 2020)
twa = Plane(seats_per_row=6, number_of_rows=25, year = 2020)