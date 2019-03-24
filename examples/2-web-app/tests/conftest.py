"""Pytest fixtures."""

from django.contrib.auth.models import User
import pytest

from testme.models import Profile


@pytest.fixture
def ex_profile(ex_user):
    """Example profile with associated user.

    Args:
        ex_user (User):  Associated user

    Returns:
        Example profile (Profile)
    """
    return Profile.objects.get(user_id=ex_user.id)


@pytest.fixture
def ex_user(db):
    """Example user.

    Args:
        db: DB access

    Returns:
        Example user (User)
    """
    user = User.objects.create(username="test_user")
    user.set_password("test")
    user.save()

    Profile.objects.create(user=user, clicks=0)

    return user


@pytest.fixture
def ex_profile_factory(db):
    """Profile factory: generate a user and a profile with a click count.

    Args:
        db: DB access

    Returns:
        Profile factory
    """
    def factory(username, clicks):
        """Inner factory.

        Args:
            username (str): Username
            clicks (int): Click count

        Returns:
            Profile with base clicks
        """
        user = User.objects.create(username=username)
        user.set_password("test")
        user.save()

        profile = Profile.objects.create(user_id=user.id, clicks=clicks)

        return profile
    return factory
