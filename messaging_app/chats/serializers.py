from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.Serializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_image']
        read_only_field = ['id']
        
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()

class MessageSerializer(serializers.Serializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'conversation', 'content', 'timestamp', 'is_read']
        read_only_fields = ['id', 'sender', 'timestamp']

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