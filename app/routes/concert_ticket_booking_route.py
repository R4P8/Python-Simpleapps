from flask import Blueprint

from app.controllers.concert_ticket_booking_controller import (
    ConcertTicketBookingController
)

concert_ticket_booking_bp = Blueprint(
    "concert_ticket_booking_bp",
    __name__
)

concert_ticket_booking_bp.route(
    "/concert-ticket-bookings",
    methods=["POST"]
)(
    ConcertTicketBookingController.create_booking
)

concert_ticket_booking_bp.route(
    "/concert-ticket-bookings",
    methods=["GET"]
)(
    ConcertTicketBookingController.get_all_bookings
)

concert_ticket_booking_bp.route(
    "/concert-ticket-bookings/<int:booking_id>",
    methods=["GET"]
)(
    ConcertTicketBookingController.get_booking_by_id
)