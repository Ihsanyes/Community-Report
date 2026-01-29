from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user'
    )

    def __str__(self):
        return self.username

class IssueReport(models.Model):

    CHOICE = [
        ('pwd', 'Road Issue / PWD'),
        ('water', 'Water Authority'),
        ('kseb', 'Electricity / KSEB'),
        ('police', 'Police Station'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CHOICE, null=True, blank=True)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    contry = models.CharField(max_length=100,  null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    landmark = models.CharField(max_length=255, null=True, blank=True)

    status = models.CharField(max_length=50,
                              choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Closed', 'Closed')],
                             default='Open')
    description = models.TextField()
    image = models.ImageField(upload_to='issue_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
