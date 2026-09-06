from tickets.models import TicketModel

class TicketService:
    @staticmethod
    def create(user, text) -> TicketModel:
        ticket = TicketModel.objects.create(
            creator=user,
            description=text,
        )

        return ticket

    @staticmethod
    def get_user_tickets(user):
        tickets = TicketModel.objects.filter(creator=user)
        return tickets