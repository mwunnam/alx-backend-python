from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    frist_name = models.TextField()
    last_name = models.TextField()
    password = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        participant_names = ', '.join([user.username for user in self.participants.all()])
        return f"Conversation ({id}): {participant_names}"

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_sent')
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message_body = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender.username} in Conversation {self.conversation_id}"