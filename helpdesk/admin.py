from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Queue)
admin.site.register(Ticket)
admin.site.register(Comment)