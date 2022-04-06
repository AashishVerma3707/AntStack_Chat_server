from django.db import models
from django.db.models import Q


class Room(models.Model):
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    group = models.CharField(max_length=80,blank=True)

    def save(self, *args, **kwargs):

        # method for categorising any two model classes having same pair of users but opposite Roles

        if Room.objects.filter(Q(sender=self.receiver) & Q(receiver=self.sender)).exists():
            obj = Room.objects.filter(Q(sender=self.receiver) & Q(receiver=self.sender))
            self.group=obj[0].group

        else:
            self.group = f"{self.sender}_{self.receiver}"

        super(Room, self).save()


class Message(models.Model):

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    time = models.DateTimeField(auto_now=True)


