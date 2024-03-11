from abc import ABC, abstractmethod

import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
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


# Abstract class. Inherited form ABC. Abstract Base Class.
# For implementing interfaces. It will force the consumer to implement needed methods.
class Ticket(ABC):
    @abstractmethod
    def generate(self):
        pass


class Reservation(Ticket):
    def __init__(self, guest_name, hotel_object):
        self.guest_name = guest_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking details:
        Name: {self.guest_name}.
        Hotel: {self.hotel.name}.
        Destination: {self.hotel.city}
        
        Wish you a nice stay!
        """
        return content


class DigitalReservation(Ticket):
    def __init__(self, guest_name, hotel_object):
        self.guest_name = guest_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your DIGITAL TICKET!
        Name: {self.guest_name}.
        Hotel: {self.hotel.name}.
        Destination: {self.hotel.city}

        Wish you a nice stay!
        """
        return content


print(df)
hotel_ID = input("Enter id of hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456", expiration="12/26", holder="JOHN SMITH", cvc="123")
    print("You entered credit card.")
    if credit_card.validate():
        print("Your credit card is validated, one time password is sent.")
        if credit_card.authenticate(given_pass="mypass"):
            print("Your credit card is authenticated.")
            hotel.book()
            name = input("Enter your name: ")
            confirmation = Reservation(guest_name=name, hotel_object=hotel)
            print(confirmation.generate())
        else:
            print("Wrong password! Credit card authentication failed")
    else:
        print("Payment problem!")
else:
    print("Hotel is not available. Choose another one.")
