from rest_framework_nested import routers
from django.contrib import admin
from django.urls import path, include
from chats.views import ConversationViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')

convo_router = routers.NestedDefaultRouter(router, r'conversations', lookup='conversation')
convo_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(convo_router.urls)),
]