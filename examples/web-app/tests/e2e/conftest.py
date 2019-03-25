"""End-to-end pytest fixtures."""

import pytest

from tests.utils import SeleniumWrapper


@pytest.fixture
def _ex_browser(live_server):
    """Fixture to create a browser instance.

    Args:
        live_server: Django live server

    Returns:
        Browser instance
    """
    live_server_url = live_server.url
    return SeleniumWrapper(live_server_url)


@pytest.fixture
def _ex_auth_browser(_ex_browser, live_server, client, ex_user):
    """Fixture to create a browser instance with an authenticated user.

    Args:
        _ex_browser: Browser instance
        live_server: Django live server
        client: Django test client
        ex_user: Example user

    Returns:
        Authenticated browser instance
    """
    browser = _ex_browser
    client.login(username=ex_user.username, password="test")

    cookie = client.cookies["sessionid"]
    browser.inner.get(live_server.url)

    # Add session ID cookie
    browser.inner.add_cookie({"name": "sessionid", "value": cookie.value, "secure": False, "path": "/"})
    # Reload page
    browser.inner.refresh()

    return browser


@pytest.fixture
def browser(_ex_browser):
    """Fixture to create a managed browser instance.

    At test end, will quit the browser.

    Args:
        _ex_browser: Browser instance

    Returns:
        Browser instance
    """
    browser = _ex_browser
    yield browser
    browser.inner.quit()


@pytest.fixture
def auth_browser(_ex_auth_browser):
    """Fixture to create a managed authenticated browser instance.

    At test end, will quit the browser.

    Args:
        _ex_auth_browser: Authenticated browser instance

    Returns:
        Authenticated browser instance
    """
    browser = _ex_auth_browser
    yield browser
    browser.inner.quit()
