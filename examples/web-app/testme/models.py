"""Models."""

import pickle

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

    def save_to_stream(self, stream):
        """Save to stream.

        Args:
            stream: Stream
        """
        stream.write(pickle.dumps({
            "user_id": self.user_id,
            "user_data": self.user_data,
            "clicks": self.clicks,
        }))

    def load_from_stream(self, stream):
        """Load from stream.

        Args:
            stream: Stream
        """
        bin_data = stream.read()
        data = pickle.loads(bin_data)

        self.user_id = data["user_id"]
        self.user_data = data["user_data"]
        self.clicks = data["clicks"]

    def __eq__(self, profile):
        return self.user.id == profile.user.id and self.user_data == profile.user_data and self.clicks == profile.clicks
