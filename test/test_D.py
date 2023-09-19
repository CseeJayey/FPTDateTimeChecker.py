import unittest
from app.DTCLib import days_in_month, is_valid_date

class TestDaysInMonth(unittest.TestCase):
    def test_valid_input_1(self):
        self.assertEqual(days_in_month(2023, 9), 30)

    def test_valid_input_leapyear(self):
        self.assertEqual(days_in_month(2023, 2), 28)
        
    def test_valid_input_nonleapyear(self):
        self.assertEqual(days_in_month(2022, 2), 28)

    def test_invalid_input_month_1(self):
        with self.assertRaises(ValueError):
            days_in_month(2023, 0)  # Month out of range

    def test_invalid_input_month_2(self):
        with self.assertRaises(ValueError):
            days_in_month(2023, 13)  # Month out of range


class TestIsValidDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(is_valid_date(2023, 9, 19))

    def test_invalid_date(self):
        self.assertFalse(is_valid_date(2023, 2, 30))


    def test_invalid_year_1(self):
        self.assertFalse(is_valid_date(10000, 9, 19))

    def test_invalid_year_2(self):
        self.assertFalse(is_valid_date(-10000, 9, 19))


    def test_invalid_month_1(self):
        self.assertFalse(is_valid_date(2023, 13, 19))

    def test_invalid_month_2(self):
        self.assertFalse(is_valid_date(2023, 0, 19))


    def test_invalid_day_1(self):
        self.assertFalse(is_valid_date(2023, 9, 32))

    def test_invalid_day_2(self):
        self.assertFalse(is_valid_date(2023, 9, 0))


    def test_valid_leapyear(self):
        self.assertTrue(is_valid_date(2000, 2, 29))

    def test_invalid_leapyear(self):
        self.assertFalse(is_valid_date(2023, 2, 29))


    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            is_valid_date("2032a", "9", "19")


if __name__ == '__main__':
    unittest.main()