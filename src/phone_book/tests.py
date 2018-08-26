import unittest
import solution


class TreeHeightTests(unittest.TestCase):
    def test_phone_book_operations(self):
        p_book = solution.PhoneBook()
        p_book.add_number("911", "police")
        p_book.add_number("76213", "Mom")
        p_book.add_number("17239", "Bob")

        self.assertEqual(p_book.find_name("76213"), "Mom")
        self.assertEqual(p_book.find_name("910"), "not found")
        self.assertEqual(p_book.find_name("911"), "police")

        p_book.del_number("910")
        p_book.del_number("911")

        self.assertEqual(p_book.find_name("911"), "not found")
        self.assertEqual(p_book.find_name("76213"), "Mom")

        p_book.add_number("76213", "daddy")
        self.assertEqual(p_book.find_name("76213"), "daddy")
