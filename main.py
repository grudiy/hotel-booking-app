import pandas

df = pandas.read_csv("hotels.csv")


class Hotel:
    def __init__(self, id):
        pass

    def book(self):
        pass

    def available(self):
        pass

class Reservation:
    def __init__(self, guest_name, hotel_object):
        pass

    def generate(self):
        pass


print(df)
id = input("Enter id of hotel: ")
hotel = Hotel(id)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    confirmation = Reservation(name, hotel)
    print(confirmation.generate())
else:
    print("Hotel is not available. Choose another one.")

