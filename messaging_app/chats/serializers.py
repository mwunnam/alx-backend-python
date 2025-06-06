from rest_framework import serializers
from rest_framework.serializers import CharField
from .models import User, Conversation, Message

class UserSerializer(serializers.Serializer):
    first_name = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['user_id', 'phone_number', 'email', 'first_name', 'last_name', 'password']
        read_only_fields = ['user_id']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()

class MessageSerializer(serializers.Serializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'conversation_id', 'message_body', 'sent_at', 'is_read']
        read_only_fields = ['id', 'sender', 'sent_at']

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message content cannot be empty.")
        return value

class CoversationSerializer(serializers.Serializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'created_at', 'messages']
        read_only_fields = ['id', 'created_at']