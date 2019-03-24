"""End to end tests."""


def test_login(browser, ex_user):
    # Go to home
    browser.navigate_to("/")

    # Should be at login url
    assert browser.check_url("/login?next=/home")

    # Get the username field
    # Enter username
    # Get the password field
    # Enter password

    # Get the submit button
    # Press submit

    # Url should now be home


# TODO: Create the test
def test_home(auth_browser):
    # Url should be home

    # Shown clicks should be at 0

    # Get the "click me" button
    # Press the button

    # Shown clicks should be at 1

    # Press the button twice

    # Shown clicks should be at 2
    pass
