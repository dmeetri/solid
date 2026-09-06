from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.TicketCreateView.as_view(), name='create_ticket'),
    path('user-list/', views.TicketListView.as_view(), name='list_tickets'),
]