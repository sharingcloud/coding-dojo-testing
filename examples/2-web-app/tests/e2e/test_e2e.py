"""End to end tests."""

import pytest


@pytest.mark.e2e
def test_login(browser, ex_user):
    from selenium.webdriver.common.keys import Keys

    # Go to home
    browser.navigate_to("/")

    # Should be at login url
    assert browser.check_url("/login?next=/home")

    # Get the username field
    username_field = browser.find_element_by_css_selector("input[name=username]")
    # Enter username
    username_field.clear()
    username_field.send_keys(ex_user.username)
    # Get the password field
    password_field = browser.find_element_by_css_selector("input[name=password]")
    # Enter password
    password_field.clear()
    password_field.send_keys("test")
    password_field.send_keys(Keys.RETURN)

    # Wait for 2 secs
    browser.wait_secs(2)
    # Url should now be home
    assert browser.check_url("/home")


# TODO: Create the test
@pytest.mark.e2e
def test_home(auth_browser):
    # Url should be home

    # Shown clicks should be at 0

    # Get the "click me" button
    # Press the button

    # Wait for 0.5 sec
    # Shown clicks should be at 1

    # Press the button twice

    # Wait for 0.5 sec
    # Shown clicks should be at 2
    pass
