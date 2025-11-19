from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class MessagingSignalsTest(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username="alice", password="test123")
        self.receiver = User.objects.create_user(username="bob", password="test123")

    def test_notification_created_on_message(self):
        """
        Vérifie que lorsqu'un Message est créé,
        une Notification est automatiquement générée.
        """
        msg = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content="Hello Bob!"
        )
        notification = Notification.objects.filter(message=msg).first()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.user, self.receiver)
        self.assertFalse(notification.is_read)

    def test_multiple_notifications(self):
        """
        Vérifie que plusieurs messages créent plusieurs notifications.
        """
        msg1 = Message.objects.create(sender=self.sender, receiver=self.receiver, content="Hi 1")
        msg2 = Message.objects.create(sender=self.sender, receiver=self.receiver, content="Hi 2")
        notifications = Notification.objects.filter(user=self.receiver)
        self.assertEqual(notifications.count(), 2)
