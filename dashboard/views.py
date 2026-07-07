from django.shortcuts import render
from django.views.generic import ListView
from .models import ticket
"""
Class-based views:

View         = Generic View
ListView     = get a list of records
DetailView   = get a single (detail) record
CreateView   = create a new record
DeleteView   = remove a record
UpdateView   = modify an existing record
LoginView    = LogIn

"""
# Create your views here.

class TicketListView(ListView):
    model = ticket
    template_name = "dashboard/all_tickets.html"