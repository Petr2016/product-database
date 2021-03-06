from django.db import models


class NotificationMessage(models.Model):
    """
    Notifications from certain processes
    """
    MESSAGE_ERROR = "ERR"
    MESSAGE_INFO = "INFO"
    MESSAGE_SUCCESS = "SUCC"
    MESSAGE_WARNING = "WARN"

    MESSAGE_TYPE = (
        ("INFO", "info"),
        ("SUCC", "success"),
        ("ERR", "error"),
        ("WARN", "warning"),
    )

    title = models.CharField(
        max_length=2048
    )

    type = models.CharField(
        max_length=8,
        choices=MESSAGE_TYPE,
        default=MESSAGE_INFO
    )

    summary_message = models.TextField(
        max_length=16384
    )

    detailed_message = models.TextField(
        max_length=16384
    )

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    @staticmethod
    def add_info_message(title, summary_message, detailed_message):
        NotificationMessage.objects.create(
            title=title,
            type=NotificationMessage.MESSAGE_INFO,
            summary_message=summary_message,
            detailed_message=detailed_message
        )

    @staticmethod
    def add_success_message(title, summary_message, detailed_message):
        NotificationMessage.objects.create(
            title=title,
            type=NotificationMessage.MESSAGE_SUCCESS,
            summary_message=summary_message,
            detailed_message=detailed_message
        )

    @staticmethod
    def add_warning_message(title, summary_message, detailed_message):
        NotificationMessage.objects.create(
            title=title,
            type=NotificationMessage.MESSAGE_WARNING,
            summary_message=summary_message,
            detailed_message=detailed_message
        )

    @staticmethod
    def add_error_message(title, summary_message, detailed_message):
        NotificationMessage.objects.create(
            title=title,
            type=NotificationMessage.MESSAGE_ERROR,
            summary_message=summary_message,
            detailed_message=detailed_message
        )

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('created',)
