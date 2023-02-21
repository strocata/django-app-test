from django.db import models
from core import models as core_models
from django.contrib.auth import get_user_model

User = get_user_model()


class Conversation(core_models.TimeStampedModel):

    """Conversation Model Definition"""

    participants = models.ManyToManyField(
        User, related_name="conversations", blank=True
    )

    def __str__(self):
        usernames = []
        for participant in self.participants.all():
            usernames.append(participant.email)
            print(" ".join(usernames))
        return ", ".join(usernames)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of participants"


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    creator = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.creator} says: {self.message}"
