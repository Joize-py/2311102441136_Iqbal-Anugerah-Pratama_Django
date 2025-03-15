from django.db import models
from django.core.exceptions import ValidationError

class Character(models.Model):
    ROLE_CHOICES = [
        ('Tank', 'Tank'),
        ('Damage', 'Damage'),
        ('Support', 'Support'),
    ]

    name = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    difficulty = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not (1 <= self.difficulty <= 3):
            raise ValidationError({'difficulty': "Difficulty must be between 1 and 3."})

    def __str__(self):
        return self.name
# Create your models here.
