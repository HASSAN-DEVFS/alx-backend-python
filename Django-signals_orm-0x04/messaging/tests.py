from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, MessageHistory, Notification


class MessagingTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username="user1")
        self.user2 = User.objects.create(username="user2")

    def test_message_creation_creates_notification(self):
        msg = Message.objects.create(sender=self.user1, receiver=self.user2, content="Hello")
        self.assertEqual(Notification.objects.filter(user=self.user2).count(), 1)

    def test_edit_message_creates_history(self):
        msg = Message.objects.create(sender=self.user1, receiver=self.user2, content="Hello")
        msg.content = "Edited"
        msg.save()
        self.assertEqual(MessageHistory.objects.filter(message=msg).count(), 1)

    def test_user_delete_cleans_related_data(self):
        Message.objects.create(sender=self.user1, receiver=self.user2, content="Hello")
        self.user1.delete()
        self.assertEqual(Message.objects.count(), 0)
