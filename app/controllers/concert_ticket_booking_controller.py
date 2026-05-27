from flask import jsonify, request

from app.services.concert_ticket_booking_service import (
    ConcertTicketBookingService
)


class ConcertTicketBookingController:

    @staticmethod
    def create_booking():

        data = request.get_json()

        booking_id = (
            ConcertTicketBookingService.create_booking(data)
        )

        return jsonify({
            "success": True,
            "message": "Booking created successfully",
            "booking_id": booking_id
        }), 201

    @staticmethod
    def get_all_bookings():

        bookings = (
            ConcertTicketBookingService.get_bookings()
        )

        return jsonify({
            "success": True,
            "data": bookings
        }), 200

    @staticmethod
    def get_booking_by_id(booking_id):

        booking = (
            ConcertTicketBookingService.get_booking(
                booking_id
            )
        )

        if not booking:
            return jsonify({
                "success": False,
                "message": "Booking not found"
            }), 404

        return jsonify({
            "success": True,
            "data": booking
        }), 200