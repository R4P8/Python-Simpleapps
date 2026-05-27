class ConcertTicketBooking:

    def __init__(
        self,
        id,
        customer_name,
        concert_name,
        venue,
        ticket_quantity,
        total_price,
        booking_date
    ):
        self.id = id
        self.customer_name = customer_name
        self.concert_name = concert_name
        self.venue = venue
        self.ticket_quantity = ticket_quantity
        self.total_price = total_price
        self.booking_date = booking_date

    def to_dict(self):
        return {
            "id": self.id,
            "customer_name": self.customer_name,
            "concert_name": self.concert_name,
            "venue": self.venue,
            "ticket_quantity": self.ticket_quantity,
            "total_price": self.total_price,
            "booking_date": str(self.booking_date)
        }