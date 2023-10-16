from django.db import models

from django.contrib.auth.models import User

PRIORITY_CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]
class Problem(models.Model):
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name