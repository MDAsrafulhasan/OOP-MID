class Star_Cinema:
    hall_list = []

    def entry_hall(self,hal):
        self.hall_list.append(hal)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.__rows = rows
        self.__cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []
        self.entry_hall(self)

    def entry_show(self,id,movie_name,time):
        show_info = (id,movie_name,time)
        self.show_list.append(show_info)

        # seats_info = [[0] * self.rows for _ in range(self.cols)]
        # self.seats[id] = seats_info

        sets = []
        for _ in range(self.__rows):
            r = [0] * self.__cols
            sets.append(r)
        self.seats[id] = sets

    def book_seats(self,id,list_of_tuples):
        if id in self.seats:
            for tuples in list_of_tuples:
                row,col = tuples
                if 0 <= row < self.__rows and 0 <= col < self.__cols:
                    if self.seats[id][row][col]==0:
                        self.seats[id][row][col]=1
                        print(f"Seat {row,col} booked successfully")
                    else:
                        print(f"Seat {row,col} is already booked")
                else:
                    print(f"Invalid seat : {row,col}")
        else:
            print("Invalid Show Id!")

    def view_show_list(self):
        print("\nRunning Shows:")
        for show_id,movie_name,show_time in self.show_list:
            print(f"Show ID: {show_id},  Movie: {movie_name},  Time: {show_time}")
   
    def view_available_seats(self,id):
        # if show_id not in self.seats:
        #     print("Invalid show ID!")
        #     return

        # print(f"\nAvailable seats for Show ID {show_id}:")
        # for row in self.seats[id]:
        #     print(row)
        if id in self.seats:
            print(f"\nAvailabel seats of Show ID {id}")
            for row in self.seats[id]:
                print(row)
        else:
            print("Invalid show ID!")


hall = Hall(7,7,1)
hall.entry_show('1','Batman','5:00 pm')
hall.entry_show('2','Spiderman','8:00 pm')

# hall.__hall_no = 0
# print(hall.__hall_no)

# hall.view_show_list()
# hall.view_available_seats()

# print(hall.__rows) 
# print(hall.__cols)
# print(hall.__hall_no) 


while True :
    print("\n_____Counter Menu_____")
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")
    # option  = input(print("Enter option : "))
    option  = input("Enter option : ")
    if option=='1':
        hall.view_show_list()
        print('\n')

    elif option=='2':
        show_id = input("Enter the show ID: ")
        hall.view_available_seats(show_id)
        # print('\n')

    elif option=='3':
        show_id = input("Enter the show ID for which you want to book seats: ")
        isit = False
        # for id,movie_name,show_time in hall.show_list:
        for show in hall.show_list:
            if show[0]==show_id:
                isit=True
                break
        if isit==True:
            seats_for_book = []
            num_of_seats = int(input("Enter the number of seats you want to book: "))
            for _ in range (num_of_seats):
                row = int(input("Enter the row number: "))
                col = int(input("Enter the column number: "))
                seats_for_book.append((row,col))
            hall.book_seats(show_id,seats_for_book)

        else:
            print("Invalid show ID!\n")

    elif option=='4':
        print("\n_______Thank you for coming_______")
        break
