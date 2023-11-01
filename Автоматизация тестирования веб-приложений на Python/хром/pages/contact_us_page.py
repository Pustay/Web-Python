from chrome.locators.contact_us_locators import ContactUsPageLocators
from chrome.pages.base_page import BasePage

class ContactUsPage(BasePage):
    locators = ContactUsPageLocators()

    input_locators: list[tuple[str, str]] = [
        locators.INPUT_NAME,
        locators.INPUT_EMAIL,
        locators.INPUT_CONTENT
    ]

    def fill_contact_us_form(self, name: str, email: str, content: str):
        for text, locator in zip([name, email, content], self.input_locators):
            self.element_is_clickable(
                locator=locator
            ).send_keys(text)

    def submit_form(self):
        self.element_is_clickable(
            locator=self.locators.SUBMIT_BUTTON
        ).click()