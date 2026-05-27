from app.repositories.concert_ticket_booking_repository import (
    ConcertTicketBookingRepository
)


class ConcertTicketBookingService:

    @staticmethod
    def create_booking(data):
        return (
            ConcertTicketBookingRepository.create_booking(data)
        )

    @staticmethod
    def get_bookings():
        return (
            ConcertTicketBookingRepository.get_all_bookings()
        )

    @staticmethod
    def get_booking(booking_id):
        return (
            ConcertTicketBookingRepository.get_booking_by_id(
                booking_id
            )
        )