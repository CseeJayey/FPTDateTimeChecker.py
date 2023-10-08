
import unittest

from app.DateTimeChecker import App


class TestGUI(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

        self.override_mb = False 


    def setUp(self):
        self.app = App()
    
    def tearDown(self):
        self.app.destroy()


    def test_check_date_valid(self):
        self.app.entry_day.insert(0, "29")
        self.app.entry_month.insert(0, "2")
        self.app.entry_year.insert(0, "2000")
        self.app.btn_check_date.event_generate('<Button-1>')

        # self.assertEqual(self.app.check_date_event(show_messagebox=self.override_mb), True)
        self.assertEqual(self.app.check_date_event(), True)

    def test_check_date_invalid(self):
        self.app.entry_day.insert(0, "12")
        self.app.entry_month.insert(0, "13")
        self.app.entry_year.insert(0, "2000")
        self.app.btn_check_date.event_generate('<Button-1>')
        
        # self.assertEqual(self.app.check_date_event(show_messagebox=self.override_mb), False)
        self.assertEqual(self.app.check_date_event(), False)

    def test_generate_random_date(self):
        self.app.rand_date_event()
        self.app.btn_check_date.event_generate('<Button-1>')

        self.assertIsNotNone(self.app.check_date_event())

    def test_check_date_general(self):
        self.app.rand_date_event()
        self.app.btn_check_date.event_generate('<Button-1>')
        
        self.assertIsNotNone(self.app.check_date_event())

        self.app.clear_entries_event()

        self.assertEqual(self.app.entry_day.get(), "")
        self.assertEqual(self.app.entry_month.get(), "")
        self.assertEqual(self.app.entry_year.get(), "")