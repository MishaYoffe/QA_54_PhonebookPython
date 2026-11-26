import logging

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

logger = logging.getLogger(__name__)

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()
        logger.info(f"Click on {locator}")

    def fill(self, locator, value):
        self.find(locator).clear()

        self.find(locator).send_keys(value)
        logger.info(f"Fill {locator} with {value}")

    def get_alert_text(self):
        alert = WebDriverWait(self.driver, timeout=10).until(

            expected_conditions.alert_is_present()

        )

        return alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

        def is_alert_visible(self):

            try:

                WebDriverWait(self.driver, timeout=10).until(

                    expected_conditions.alert_is_present()

                )

                return True

            except TimeoutException:

                return False

    def is_alert_visible(self):

        try:

            WebDriverWait(self.driver, timeout=10).until(

                expected_conditions.alert_is_present()

            )

            return True

        except TimeoutException:

            return False



