from django.contrib import admin
from . import models


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """Conversation Admin Definition"""

    filter_horizontal = ("participants",)

    list_display = ("__str__", "count_messages", "count_participants")


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """Message Admin Definition"""

    pass
