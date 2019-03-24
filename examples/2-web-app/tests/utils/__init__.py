from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumWrapper(object):
    """Selenium wrapper."""

    def __init__(self, base_url):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.inner = webdriver.Chrome(options=options)
        self.base_url = base_url
        self.wait_timeout = 5

        self.touch_actions = webdriver.TouchActions(self.inner)

    def check_url(self, url):
        """Check url."""
        return self.inner.current_url == f"{self.base_url}{url}"

    @property
    def error_logs(self):
        """Get JS error logs from browser."""
        return [x for x in self.inner.get_log("browser") if x["source"] == "javascript" and x["level"] == "SEVERE"]

    def execute_script(self, code, *args):
        """Execute JS script."""
        self.inner.execute_script(code, *args)

    def navigate_to(self, url):
        """Navigate to URLs."""
        self.inner.get(f"{self.base_url}{url}")

    ################
    # Wait functions

    def wait_for(self, condition, wait_timeout=None):
        """Wait for a condition."""
        wait_timeout = wait_timeout or self.wait_timeout

        try:
            wait = WebDriverWait(self.inner, wait_timeout)
            ret_value = wait.until(condition)
            return ret_value
        except Exception:
            pass

    def wait_secs(self, secs):
        """Wait for secs."""
        return self.wait_for(lambda x: False, secs)

    def wait_visible_element(self, by, elem):
        """Wait for visible element."""
        return self.wait_for(EC.visibility_of_element_located((by, elem)))

    def wait_clickable_element(self, by, elem):
        """Wait for clickable element."""
        return self.wait_for(EC.element_to_be_clickable((by, elem)))

    def wait_url_change(self, url):
        """Wait URL change."""
        return self.wait_for(lambda x: self.check_url(url))
