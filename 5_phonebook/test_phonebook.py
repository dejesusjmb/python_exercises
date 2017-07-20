import unittest
import os

import phonebook


class TestPhonebook(unittest.TestCase):

    def setUp(self):
        phonebook.clear()

    def test_add_and_get(self):
        self._verify_add_and_get("Toffee", "09989660750")
        self._verify_add_and_get("Maria", "09989661302")

    def _verify_add_and_get(self, name, number):
        self.assertEquals(phonebook.add(name, number), True)
        self.assertEquals(phonebook.get(name), number)

    def test_get_non_existing_name(self):
        self._verify_name_non_existing("NonExistingName")

    def _verify_name_non_existing(self, name):
        self.assertRaises(phonebook.NameNotExistError, phonebook.get, name)

    def test_clear(self):
        phonebook.add("name", "09989661302")
        phonebook.clear()
        self._verify_name_non_existing("name")

    def test_empty_book_to_string(self):
        self.assertEquals(phonebook.serialize(), "")

    def test_serialize_to_string(self):
        self._add_test_names()
        self.assertEquals(phonebook.serialize(), self.TEST_NAMES_SERIALIZED)

    def test_read_from_string(self):
        phonebook.deserialize(self.TEST_NAMES_SERIALIZED)
        print phonebook.book
        self._verify_test_names()

    def test_save_and_read_from_file(self):
        self._add_test_names()
        phonebook.save("test.temp")
        phonebook.clear()
        phonebook.load("test.temp")
        self._verify_test_names()
        os.remove("test.temp")

    TEST_NAMES_SERIALIZED = """John=09987654321
Name=09123456789
"""

    def _add_test_names(self):
        phonebook.add("Name", "09123456789")
        phonebook.add("John", "09987654321")

    def _verify_number(self, name, number):
        self.assertEquals(phonebook.get(name), number)

    def _verify_test_names(self):
        self._verify_number("Name", "09123456789")
        self._verify_number("John", "09987654321")

    def test_adding_illegal_numbers(self):
        self._verify_not_added("Illegal", "not valid", phonebook.InvalidInputException, "Invalid number")
        self._verify_not_added("Illegal", "123=12", phonebook.InvalidInputException, "Invalid number")
        self._verify_not_added("Illegal", "123 + 123", phonebook.InvalidInputException, "Invalid number")
        self._verify_not_added("Illegal", "", phonebook.InvalidInputException, "Invalid number")

    def test_adding_illegal_names(self):
        self._verify_not_added("Joe==Doe", "09987654321", phonebook.InvalidInputException, "Invalid name")
        self._verify_not_added("Joe !#%&", "09987654321", phonebook.InvalidInputException, "Invalid name")
        self._verify_not_added("", "09987654321", phonebook.InvalidInputException, "Invalid name")

    def test_duplicate_add(self):
        self._add_test_names()
        self.assertRaises(phonebook.NameAlreadyInPhonebookError, phonebook.add, "Name", "anyNumber")
        self.assertRaises(phonebook.NameAlreadyInPhonebookError, phonebook.add, "John", "anyNumber")


    def _verify_not_added(self, name, number, error, errorMsg):
        self._verify_invalid_add(name, number, error, errorMsg)
        self._verify_name_non_existing(name)

    def _verify_invalid_add(self, name, number, error, errorMsg):
        try:
            phonebook.add(name, number)
        except error as e:
            self.assertEquals(e.message, errorMsg)

if __name__ == "__main__":
    unittest.main()
