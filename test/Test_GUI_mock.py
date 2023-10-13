
import unittest

from app.DateTimeChecker import App

from customtkinter import CTkEntry


def tkinter_set_text(entry: CTkEntry, text: str):
    entry.delete(0, "end")
    entry.insert(0, text)

class TestGUI(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        
        self.override_mb = False 


    @classmethod
    def setUpClass(self):
        self.app = App()
    
    @classmethod
    def tearDownClass(self):
        self.app.destroy()


    def test_check_date_valid(self):
        tkinter_set_text(self.app.entry_day, "29")
        tkinter_set_text(self.app.entry_month, "2")
        tkinter_set_text(self.app.entry_year, "2000")
        self.app.btn_check_date.event_generate('<Button-1>')

        self.assertEqual(self.app.check_date_event(show_messagebox=self.override_mb), True)

    def test_check_date_invalid(self):
        tkinter_set_text(self.app.entry_day, "12")
        tkinter_set_text(self.app.entry_month, "13")
        tkinter_set_text(self.app.entry_year, "2000")
        self.app.btn_check_date.event_generate('<Button-1>')
        
        self.assertEqual(self.app.check_date_event(show_messagebox=self.override_mb), False)

    def test_generate_random_date(self):
        self.app.rand_date_event()
        self.app.btn_check_date.event_generate('<Button-1>')

        self.assertIsNotNone(self.app.check_date_event(show_messagebox=self.override_mb))

    def test_check_date_general(self):
        self.app.rand_date_event()
        self.app.btn_check_date.event_generate('<Button-1>')
        
        self.assertIsNotNone(self.app.check_date_event(show_messagebox=self.override_mb))

        self.app.clear_entries_event()

        self.assertEqual(self.app.entry_day.get(), "")
        self.assertEqual(self.app.entry_month.get(), "")
        self.assertEqual(self.app.entry_year.get(), "")