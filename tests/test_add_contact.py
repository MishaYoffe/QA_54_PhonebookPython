import logging
import random

from models.contact import Contact

from pages.add_contact_page import ContactPage

from faker import Faker

fake = Faker()
logger = logging.getLogger(__name__)


def test_add_contact_success(authenticated):
    logger.info(f"test_add_contact_success")
    contact_page = ContactPage(authenticated)
    random_suffix = random.randint(10000, 1000000)

    contact = Contact(
         "Michael",
        "Smith",
        f"05367{random_suffix}",
        f"test_{random_suffix}@gm.com",
        "TelAviv",
        "QA"
    )



    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)

def test_add_contact_success_all_req_fields(authenticated):
    contact_page = ContactPage(authenticated)

    random_suffix = random.randint(10000, 1000000)

    contact = Contact(

        "Kristina",

        "Test",

        f"05435{random_suffix}",

        f"test_{random_suffix}@gm.com",

        "TelAviv",

        "")

         #name = fake.first_name(),
         #last_name = fake.last_name(),
         #phone=f"05435{random_suffix}",
         #phone = fake.numerify("05#########"),
         #email = fake.email(),
         #address = fake.street_address(),
         #description = "")


    contact_page.open_contact_form()

    contact_page.fill_contact_form(contact)

    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)



