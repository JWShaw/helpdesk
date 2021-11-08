from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Queue

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'helpdesk/index.html'
    context_object_name = 'queues_list'

    def get_queryset(self):
        return Queue.objects

def queues(request):
    return HttpResponse("All queues here")

def queue(request, queue_id):
    return HttpResponse("Looking at the following queue: %s" % queue_id)


