from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError

from .models import TicketModel
from .services import TicketService
from .forms import TicketCreateForm

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = TicketModel
    form_class = TicketCreateForm
    template_name = 'tickets/create.html'
    success_url = reverse_lazy('ticket-list')

    def form_valid(self, form):
        try:
            self.object = TicketService.create(
                user=self.request.user,
                text=form.cleaned_data['text']
            )
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error('text', e.message)
            return self.form_invalid(form)


class TicketListView(LoginRequiredMixin, ListView):
    model = TicketModel
    template_name = 'tickets/list.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        tickets = TicketService.get_user_tickets(self.request.user)
        return tickets
