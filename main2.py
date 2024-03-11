# For experiments with OOP

import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    watermark = "Booking Company Name"

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        self.city = df.loc[df["id"] == self.hotel_id, "city"].squeeze()

    def book(self):
        """Book a hotel, changing the availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if hotel available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    # class method
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)


class Reservation:
    def __init__(self, guest_name, hotel_object):
        self.guest_name = guest_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking details:
        Name: {self.the_guest_property}.
        Hotel: {self.hotel.name}.
        Destination: {self.hotel.city}
        
        Wish you a nice stay!
        """
        return content

    # Property. Defined as a method, but called like a variable
    @property
    def the_guest_property(self):
        name = self.guest_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2



hotel1 = Hotel(hotel_id="134")
hotel2 = Hotel(hotel_id="655")

print(hotel1.name)
print(hotel2.name)

print(hotel1.watermark)
print(hotel2.watermark)

print(Hotel.watermark)

print(Hotel.get_hotel_count(data=df))
print(hotel1.get_hotel_count(data=df))

reservation = Reservation(guest_name="john smith  ", hotel_object=hotel1)
print(reservation.the_guest_property)
print(reservation.generate())

print(reservation.convert(100))