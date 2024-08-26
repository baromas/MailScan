from django.db import models


class MailClient(models.Model):
    SERVICE_CHOICES = [
        ('yandex', 'Yandex'),
        ('gmail', 'Gmail'),
        ('mailru', 'Mail.ru'),
    ]

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    service = models.CharField(max_length=10, choices=SERVICE_CHOICES)
    imap_server = models.CharField(max_length=255)
    imap_port = models.IntegerField(default=993)

    def __str__(self):
        return f"{self.email} ({self.service})"


class EmailMessage(models.Model):
    client = models.ForeignKey(MailClient, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    sent_date = models.DateTimeField()
    received_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return f"{self.subject} (from {self.client.email})"


class EmailAttachment(models.Model):
    message = models.ForeignKey(EmailMessage, related_name='attachments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')

    def __str__(self):
        return f"File {self.file.name} (from {self.message})"
