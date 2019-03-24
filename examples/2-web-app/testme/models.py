"""Models."""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_data = models.CharField(max_length=255, default='')
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return (
            f"[{self.user}] {self.clicks} click(s)"
        )

    def add_click(self):
        """Add one click."""
        self.clicks += 1
        self.save()

    def reset_clicks(self):
        """Reset clicks."""
        self.clicks = 0
        self.save()
