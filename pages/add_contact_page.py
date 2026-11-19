from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from models.contact import  Contact



class ContactPage(BasePage):
    ADD_CONTACT_BUTTON = (By.CSS_SELECTOR, "[href='/add']")

    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")

    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")

    PHOHE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone']")

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='email']")

    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address']")

    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "input[placeholder='description']")

    SAVE_BUTTON = (By.XPATH, "//button[contains(., 'Save')]")


    def __init__(self, driver):
        self.driver = driver

    def open_contact_form(self):
        self.click(self, self.ADD_CONTACT_BUTTON).click()

    def fill_name(self, name):
        #self.driver.find_element(*self.NAME_INPUT).clear()
        #self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.fill(self.NAME_INPUT,name)

    def fill_last_name(self, last_name):
        #self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        #self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.fill(self.LAST_NAME_INPUT,last_name)

    def fill_address(self, address):
        #self.driver.find_element(*self.ADDRESS_INPUTRESS_INPUT).clear()
        #self.driver.find_element(*self.ADDRESS_INPUTDRESS_INPUT).send_keys(address)
        self.fill(self.ADDRESS_INPUTRESS,address)

    def fill_description(self, description):
        #self.driver.find_element(*self.DESCRIPTION_INPUT).clear()

        #self.driver.find_element(*self.DESCRIPTION_INPUT).send_keys(description)
        self.fill(self.DESCRIPTION,description)


    def fill_contact_form(self, contact):
        self.fill_name(contact.name)

        self.fill_last_name(contact.last_name)

        self.fill_phone(contact.phone)

        self.fill_email(contact.email)

        self.fill_address(contact.address)

        self.fill_description(contact.description)


    def submit_contact(self):
        #self.driver.find_element(*self.SAVE_BUTTON).click()
        self.click(self.SAVE_BUTTON)


    def contact_card_visible(self, phone):
        locator = (By.XPATH, f"//h3[contains(text(),'{phone}')]")

        element = WebDriverWait(self.driver, 5).until(

            expected_conditions.presence_of_element_located(locator))

        return element.is_displayed()

    def open_contact_details_card(self, phone):
        card = self.driver.find_element(By.XPATH, f"//h3[contains(text(),'{phone}')]/..").click()

    def create_contact_steps(self, contact):
        self.open_contact_form()

        self.fill_contact_form(contact)

        self.submit_contact()



