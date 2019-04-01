"""Test profile."""

import os

from testme.models import Profile


def test_profile_default(ex_user):
    # A new user should have a profile by default
    assert Profile.objects.filter(user_id=ex_user.id).count() == 1


def test_profile_zero_clicks(ex_profile):
    # Clicks should be at 0 by default
    assert ex_profile.clicks == 0


def test_profile_add_click(ex_profile_factory):
    # Create a profile with no initial clicks
    profile_zero = ex_profile_factory("test1", 0)
    # The add_click method should add 1 to clicks
    profile_zero.add_click()
    assert profile_zero.clicks == 1

    # Create a profile with 1000 initial clicks
    profile = ex_profile_factory("test2", 1000)
    # The add_click method should add 1 to clicks
    profile.add_click()
    assert profile.clicks == 1001


# TODO: Create the test
def test_profile_reset_clicks(ex_profile_factory):
    # Create a profile with no initial clicks
    # The reset_clicks should reset clicks to 0

    # Create a profile with 1000 initial clicks
    # The reset_clicks should reset clicks to 0
    assert False


# TODO: Continue the test
def test_profile_clicks_to_stream(ex_profile_factory, tmpdir):
    # Create a new profile
    profile: Profile = ex_profile_factory("test", 50)
    # Create a temporary directory
    # Create a file in this directory
    path_to_file = os.path.join(tmpdir, "example.bin")
    # Open the file
    with open(path_to_file, mode="wb") as stream:
        # Save the clicks to the stream
        profile.save_to_stream(stream)

    # Create another profile with more clicks
    # Open the previous file
    # load the clicks from the stream

    # Assert that the two profiles are the same
    assert False
