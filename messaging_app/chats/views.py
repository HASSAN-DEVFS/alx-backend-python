from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import MessageSerializer
from .permissions import IsOwner


# class ConversationViewSet(viewsets.ModelViewSet):
#     queryset = Conversation.objects.all()
#     serializer_class = ConversationSerializer

#     @action(detail=True, methods=['post'])
#     def add_message(self, request, pk=None):
#         conversation = self.get_object()
#         message_body = request.data.get('message_body')
#         sender = request.user  # si auth activée
#         message = Message.objects.create(
#             conversation=conversation,
#             sender=sender,
#             message_body=message_body
#         )
#         return Response(MessageSerializer(message).data)




class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Message.objects.filter(user=self.request.user)

