import unittest
from app.DTCLib import days_in_month, is_valid_date

class TestDaysInMonth(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(days_in_month(2023, 9), 30)
        self.assertEqual(days_in_month(1960, 1), 31)

    def test_valid_input_leapyear(self):
        self.assertEqual(days_in_month(2020, 2), 29)
        self.assertEqual(days_in_month(2000, 2), 29)
        
    def test_valid_input_nonleapyear(self):
        self.assertEqual(days_in_month(2022, 2), 28)
        self.assertEqual(days_in_month(1500, 2), 28)

    def test_invalid_input_month(self):
        with self.assertRaises(ValueError):
            days_in_month(2023, 0)
        with self.assertRaises(ValueError):
            days_in_month(2023, 13)


class TestIsValidDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(is_valid_date(2023, 9, 19))
        self.assertTrue(is_valid_date(2020, 2, 29))

    def test_invalid_date(self):
        self.assertFalse(is_valid_date(2023, 2, 30))
        self.assertFalse(is_valid_date(2023, -1, 0))


    def test_out_of_range_year(self):
        self.assertFalse(is_valid_date(10000, 9, 19))
        self.assertFalse(is_valid_date(-10000, 9, 19))


    def test_out_of_range_month(self):
        self.assertFalse(is_valid_date(2023, 13, 19))
        self.assertFalse(is_valid_date(2023, 0, 19))


    def test_out_of_range_day(self):
        self.assertFalse(is_valid_date(2023, 9, 32))
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