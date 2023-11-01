from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    @staticmethod
    def format_locator(locator, text):
        return locator[0], locator[-1].format(text=text)

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self) -> None:
        self.driver.get(self.url)

    def go_to_element(self, element) -> bool:
        try:
            self.driver.execute_script('arguments[0].scrollIntoView();', element)
        except NoSuchElementException:
            return False
        return True

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def is_element_visible(self, locator, timeout=5) -> bool:
        try:
            self.go_to_element(self.element_is_present(locator))
            wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    def get_alert_text(self, timeout=5) -> str:
        alert = wait(self.driver, timeout).until(EC.alert_is_present())
        try:
            alert_text = alert.text
        finally:
            alert.accept()
        return alert_text