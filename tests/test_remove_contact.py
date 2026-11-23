import logging

from pages.contacts_page import ContactsPage

logger = logging.getLogger(__name__)


def test_remove_contact(ensure_min_contacts):
    logger.info(f"test_remove_contact")

    contacts_page = ContactsPage(ensure_min_contacts)

    contacts_page.open_contacts_list()

    count_before = contacts_page.get_contact_cards_number()

    logger.info(f"Contacts before delete: {count_before}")

    contacts_page.open_first_contact()

    contacts_page.remove_current_contact()

    count_after = contacts_page.get_contact_cards_number()

    logger.info(f"Contacts after delete: {count_after}")

    assert count_after == count_before - 1


def test_remove_all_contacts(ensure_min_contacts):
    contacts_page = ContactsPage(ensure_min_contacts)

    contacts_page.open_contacts_list()

    contacts_page.remove_all_contacts()

    assert contacts_page.get_contact_cards_number()==0




