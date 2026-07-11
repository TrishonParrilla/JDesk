from django.urls import path

from pages.views import AboutPageView, HomePageView, TrialTicketView
 

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('trial-ticket/', TrialTicketView.as_view(), name='trial_ticket'),
]