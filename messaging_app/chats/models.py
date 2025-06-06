from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username

class Message(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="message_sent",
    )
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASACADE,
        related_name="message_sent",
    )
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = modles.BooleanFieal(default=False)

    def __str__(str):
        return f"Message from {self.sender.username} in chat with id{self.conversation.id}"


class Conversation(models.Model):
    participants = models.ManyToManyField(
        User,
        related_name=
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):


