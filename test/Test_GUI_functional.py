import os
import subprocess
from time import sleep
import unittest
from datetime import date
import pyautogui


class Action():
    def __init__(self, x, y, duration, input) -> None:
        self.x: int = x
        self.y: int = y
        self.duration: float = duration
        self.input = input
    
    def __str__(self) -> str:
        return f"({self.__class__.__name__}) x: {self.x}, y: {self.y}, duration: {self.duration}, input: {self.input}"


class TestGUI(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.click_duration = 0.05
        self.widget_pos = {
            "day_txtbox" : (207, 462),
            "month_txtbox" : (406, 462),
            "year_txtbox" : (608, 462),
            "check_btn" : (608, 520),
            "clear_btn" : (204, 520),
            "generate_btn" : (406, 587),
            "exit_btn" : (687, 314),
            "logo_img" : (207, 350),
        }

    @classmethod
    def setUpClass(self):
        root_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        app_path = os.path.join(root_dir, 'main.py')
        self.app_process = subprocess.Popen(["python", app_path])
        sleep(1)
        
    @classmethod
    def tearDownClass(self):
        self.app_process.terminate()

    def test_1_GUI_change_logo(self):
        actions = {
            "logo_img_click": Action(self.widget_pos.get("logo_img")[0], self.widget_pos.get("logo_img")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "logo_img_click1": Action(self.widget_pos.get("logo_img")[0], self.widget_pos.get("logo_img")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
        }
        for p in actions:
            pyautogui.moveTo(actions.get(p).x, actions.get(p).y, actions.get(p).duration)
            if actions.get(p).input is not None: actions.get(p).input()

    def test_2_GUI_check_invalid(self):
        actions = {
            "check_btn_click": Action(self.widget_pos.get("check_btn")[0], self.widget_pos.get("check_btn")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "confirm_dialog_enter": Action(self.widget_pos.get("check_btn")[0], self.widget_pos.get("check_btn")[1], 1, 
                                lambda : pyautogui.press("enter")),

            "day_txtbox_click": Action(self.widget_pos.get("day_txtbox")[0], self.widget_pos.get("day_txtbox")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "day_input": Action(self.widget_pos.get("day_txtbox")[0], self.widget_pos.get("day_txtbox")[1], 0.5, 
                                lambda : pyautogui.typewrite("29")),

            "month_txtbox_click": Action(self.widget_pos.get("month_txtbox")[0], self.widget_pos.get("month_txtbox")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "month_input": Action(self.widget_pos.get("month_txtbox")[0], self.widget_pos.get("month_txtbox")[1], 0.5, 
                                lambda : pyautogui.typewrite("2")),

            "year_txtbox_click": Action(self.widget_pos.get("year_txtbox")[0], self.widget_pos.get("year_txtbox")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "year_input": Action(self.widget_pos.get("year_txtbox")[0], self.widget_pos.get("year_txtbox")[1], 0.5, 
                                lambda : pyautogui.typewrite("2021")),

            "check_btn_click1": Action(self.widget_pos.get("check_btn")[0], self.widget_pos.get("check_btn")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "confirm_dialog_enter1": Action(self.widget_pos.get("check_btn")[0], self.widget_pos.get("check_btn")[1], 1, 
                                lambda : pyautogui.press("enter")),
            
            "clear_btn_click": Action(self.widget_pos.get("clear_btn")[0], self.widget_pos.get("clear_btn")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
        }
        for p in actions:
            pyautogui.moveTo(actions.get(p).x, actions.get(p).y, actions.get(p).duration)
            if actions.get(p).input is not None: actions.get(p).input()

    def test_3_GUI_check_outofrange(self):
        actions = {
            "day_txtbox_click": Action(self.widget_pos.get("day_txtbox")[0], self.widget_pos.get("day_txtbox")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "day_input": Action(self.widget_pos.get("day_txtbox")[0], self.widget_pos.get("day_txtbox")[1], 0.5, 
                                lambda : pyautogui.typewrite("42")),

            "month_txtbox_click": Action(self.widget_pos.get("month_txtbox")[0], self.widget_pos.get("month_txtbox")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "month_input": Action(self.widget_pos.get("month_txtbox")[0], self.widget_pos.get("month_txtbox")[1], 0.5, 
                                lambda : pyautogui.typewrite("122")),

            "year_txtbox_click": Action(self.widget_pos.get("year_txtbox")[0], self.widget_pos.get("year_txtbox")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "year_input": Action(self.widget_pos.get("year_txtbox")[0], self.widget_pos.get("year_txtbox")[1], 0.5, 
                                lambda : pyautogui.typewrite("2021")),

            "check_btn_click1": Action(self.widget_pos.get("check_btn")[0], self.widget_pos.get("check_btn")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "confirm_dialog_enter1": Action(self.widget_pos.get("check_btn")[0], self.widget_pos.get("check_btn")[1], 1, 
                                lambda : pyautogui.press("enter")),
            
            "clear_btn_click": Action(self.widget_pos.get("clear_btn")[0], self.widget_pos.get("clear_btn")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
        }
        for p in actions:
            pyautogui.moveTo(actions.get(p).x, actions.get(p).y, actions.get(p).duration)
            if actions.get(p).input is not None: actions.get(p).input()

    def test_4_GUI_check_typeErr(self):
        actions = {
            "day_txtbox_click": Action(self.widget_pos.get("day_txtbox")[0], self.widget_pos.get("day_txtbox")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "day_input": Action(self.widget_pos.get("day_txtbox")[0], self.widget_pos.get("day_txtbox")[1], 0.5, 
                                lambda : pyautogui.typewrite("12")),

            "month_txtbox_click": Action(self.widget_pos.get("month_txtbox")[0], self.widget_pos.get("month_txtbox")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "month_input": Action(self.widget_pos.get("month_txtbox")[0], self.widget_pos.get("month_txtbox")[1], 0.5, 
                                lambda : pyautogui.typewrite("@!#*&(!)")),

            "year_txtbox_click": Action(self.widget_pos.get("year_txtbox")[0], self.widget_pos.get("year_txtbox")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "year_input": Action(self.widget_pos.get("year_txtbox")[0], self.widget_pos.get("year_txtbox")[1], 0.5, 
                                lambda : pyautogui.typewrite("2008")),

            "check_btn_click1": Action(self.widget_pos.get("check_btn")[0], self.widget_pos.get("check_btn")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "confirm_dialog_enter1": Action(self.widget_pos.get("check_btn")[0], self.widget_pos.get("check_btn")[1], 1, 
                                lambda : pyautogui.press("enter")),
            
            "clear_btn_click": Action(self.widget_pos.get("clear_btn")[0], self.widget_pos.get("clear_btn")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
        }
        for p in actions:
            pyautogui.moveTo(actions.get(p).x, actions.get(p).y, actions.get(p).duration)
            if actions.get(p).input is not None: actions.get(p).input()

    def test_5_GUI_general(self):
        today = date.today()
        day = str(today.day)
        month = str(today.month)
        year = str(today.year)
        actions = {
            "day_txtbox_click": Action(self.widget_pos.get("day_txtbox")[0], self.widget_pos.get("day_txtbox")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "day_input": Action(self.widget_pos.get("day_txtbox")[0], self.widget_pos.get("day_txtbox")[1], 0.5, 
                                lambda : pyautogui.typewrite(day)),

            "month_txtbox_click": Action(self.widget_pos.get("month_txtbox")[0], self.widget_pos.get("month_txtbox")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "month_input": Action(self.widget_pos.get("month_txtbox")[0], self.widget_pos.get("month_txtbox")[1], 0.5, 
                                lambda : pyautogui.typewrite(month)),

            "year_txtbox_click": Action(self.widget_pos.get("year_txtbox")[0], self.widget_pos.get("year_txtbox")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "year_input": Action(self.widget_pos.get("year_txtbox")[0], self.widget_pos.get("year_txtbox")[1], 0.5, 
                                lambda : pyautogui.typewrite(year)),

            "check_btn_click": Action(self.widget_pos.get("check_btn")[0], self.widget_pos.get("check_btn")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "confirm_dialog_enter": Action(self.widget_pos.get("check_btn")[0], self.widget_pos.get("check_btn")[1], 1, 
                                lambda : pyautogui.press("enter")),
            
            "clear_btn_click": Action(self.widget_pos.get("clear_btn")[0], self.widget_pos.get("clear_btn")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
        }
        for p in actions:
            pyautogui.moveTo(actions.get(p).x, actions.get(p).y, actions.get(p).duration)
            if actions.get(p).input is not None: actions.get(p).input()

    def test_6_GUI_generate(self):
        actions = {
            "generate_btn_click": Action(self.widget_pos.get("generate_btn")[0], self.widget_pos.get("generate_btn")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "generate_btn_click1": Action(self.widget_pos.get("generate_btn")[0], self.widget_pos.get("generate_btn")[1], 0.2, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "generate_btn_click2": Action(self.widget_pos.get("generate_btn")[0], self.widget_pos.get("generate_btn")[1], 0.2, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "check_btn_click": Action(self.widget_pos.get("check_btn")[0], self.widget_pos.get("check_btn")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "confirm_dialog_enter": Action(self.widget_pos.get("check_btn")[0], self.widget_pos.get("check_btn")[1], 1, 
                                lambda : pyautogui.press("enter")),
            "clear_btn_click": Action(self.widget_pos.get("clear_btn")[0], self.widget_pos.get("clear_btn")[1], 0.5, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
        }
        for p in actions:
            pyautogui.moveTo(actions.get(p).x, actions.get(p).y, actions.get(p).duration)
            if actions.get(p).input is not None: actions.get(p).input()

    def test_7_GUI_exit(self):
        actions = {
            "generate_btn_click": Action(self.widget_pos.get("exit_btn")[0], self.widget_pos.get("exit_btn")[1], 0.2, 
                                lambda : pyautogui.leftClick(duration=self.click_duration)),
            "confirm_dialog_enter": Action(self.widget_pos.get("exit_btn")[0], self.widget_pos.get("exit_btn")[1], 1, 
                                lambda : pyautogui.press("enter")),
        }
        for p in actions:
            pyautogui.moveTo(actions.get(p).x, actions.get(p).y, actions.get(p).duration)
            if actions.get(p).input is not None: actions.get(p).input()

