from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError

from .models import TicketModel
from .services import TicketService

def index(request):
    return render(request, 'index.html')

#--- TICKET CRUD ---

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = TicketModel
    #form_class = TicketCreateForm
    template_name = 'tickets/create.html'
    success_url = reverse_lazy('ticket-list') # тут сделать страницу, где отображены все тикеты пользователя

    def form_valid(self, form):
        try:
            self.object = TicketService.create(
                user=self.request.user,
                text=form.cleaned_data['text']
            )
            return super().form_valid(form)  # или редирект на success_url
        except ValidationError as e:
            form.add_error('text', e.message)
            return self.form_invalid(form)