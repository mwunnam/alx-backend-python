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

class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        participant_names = ', '.join([user.username for user in self.participants.all()])
        return f"Conversation ({self.id}): {participant_names}"

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_sent')
    Conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender.username} in Conversation {self.conversation.id}"