from tickets.models import TicketModel

class TicketService:
    @staticmethod
    def create(user, text) -> TicketModel:
        ticket = TicketModel.objects.create(
            creator=user,
            description=text,
        )

        return ticket