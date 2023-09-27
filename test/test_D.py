import unittest
from app.DTCLib import days_in_month, is_valid_date

class TestDaysInMonth(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

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
    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def test_valid_date(self):
        err = "Date is invalid."
        self.assertTrue(is_valid_date(2023, 9, 19), msg=err)
        self.assertTrue(is_valid_date(2020, 2, 29), msg=err)

    def test_invalid_date(self):
        err = "Date is valid."
        self.assertFalse(is_valid_date(2023, 2, 30), msg=err)
        self.assertFalse(is_valid_date(2023, -1, 0, msg=err))


    def test_out_of_range_year(self):
        err = "Year not out of range."
        self.assertFalse(is_valid_date(10000, 9, 19), msg=err)
        self.assertFalse(is_valid_date(-10000, 9, 19), msg=err)
        self.assertFalse(is_valid_date(-1000, 9, 19), msg=err)


    def test_out_of_range_month(self):
        err = "Month not out of range."
        self.assertFalse(is_valid_date(2023, 13, 19), msg=err)
        self.assertFalse(is_valid_date(2023, 0, 19), msg=err)


    def test_out_of_range_day(self):
        err = "Day not out of range."
        self.assertFalse(is_valid_date(2023, 9, 32), msg=err)
        self.assertFalse(is_valid_date(2023, 9, 0), msg=err)


    def test_valid_leapyear(self):
        err = "Not a leap year."
        self.assertTrue(is_valid_date(2000, 2, 29), msg=err)
        self.assertTrue(is_valid_date(2020, 2, 29), msg=err)

    def test_invalid_leapyear(self):
        err = "Is a leap year."
        self.assertFalse(is_valid_date(2023, 2, 29), msg=err)
        self.assertFalse(is_valid_date(2025, 2, 29), msg=err)


    def test_non_numeric_input(self):
        err = "Valid input."
        with self.assertRaises(ValueError, msg=err):
            is_valid_date("a", "b", "c")
        with self.assertRaises(ValueError, msg=err):
            is_valid_date("2032a", "b", "c")
        with self.assertRaises(ValueError, msg=err):
            is_valid_date("2032a", "$#", "19.2")


# if __name__ == '__main__':
#     unittest.main()