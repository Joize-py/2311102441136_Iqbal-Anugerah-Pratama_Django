from django.db import models
from django.core.exceptions import ValidationError


# Models tier
class Karakter(models.Model):
    ROLE_CHOICES = [
        ('Tank', 'Tank'),
        ('Damage', 'Damage'),
        ('Support', 'Support'),
    ]

    TIER_CHOICES = [
        ('S', 'S'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    name = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    difficulty = models.IntegerField(blank=True, null=True)
    tier = models.CharField(max_length=1, choices=TIER_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not (1 <= self.difficulty <= 3):
            raise ValidationError({'difficulty': "Difficulty must be between 1 and 3."})

    def __str__(self):
        return self.name
    

# Models karakter
class Hero(models.Model):
    ROLE_CHOICES = [
        ('Tank', 'Tank'),
        ('Damage', 'Damage'),
        ('Support', 'Support'),
    ]

    TIER_CHOICES = [
        ('S', 'S'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),   
    ]

    name = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    tier = models.CharField(max_length=1, choices=TIER_CHOICES, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
