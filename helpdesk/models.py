from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Queue(models.Model):
    queue_name = models.CharField(max_length=32)
    subscribers = models.ManyToManyField(User)

    def __str__(self):
        return self.queue_name

class Ticket(models.Model):
    creator = models.ForeignKey(User, editable=False, null=True, on_delete=models.SET_NULL, related_name="ticket_creator")
    assignee = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="ticket_assignee")
    ticket_name = models.CharField(max_length=32)
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "%s: %s" % (self.queue, self.ticket_name)

class Comment(models.Model):
    commenter = models.ForeignKey(User, editable=False, null=True, on_delete=models.SET_NULL)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    comment_text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "%s: %s..." % (self.commenter, self.comment_text)