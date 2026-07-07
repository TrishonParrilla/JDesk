from django.urls import path
from . import views

urlpatterns = [
    path('all_tickets', views.TicketListView.as_view(), name='ticket_list')
]