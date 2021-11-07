from django.urls import path

from . import views

app_name = 'helpdesk'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # Show just the tickets for a given queue
    path('queues/<int:pk>/tickets', views.IndexView.as_view(), name='queue')
]
