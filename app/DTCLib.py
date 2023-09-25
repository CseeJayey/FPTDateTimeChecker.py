import calendar
import random
from tkinter import messagebox
from customtkinter import CTkEntry

Config = {
    "window_title": "Date Time Checker",
    "window_size": "600x300",
    "logo_path0": "./app/images/logo0.png",
    "logo_path1": "./app/images/logo1.png",
    "logo_path2": "./app/images/logo2.png",
    "logo_size": (250, 70),
}

def days_in_month(year: int, month: int):
    return calendar.monthrange(year, month)[1]

def is_valid_date(year: int, month: int, day: int, show_messagebox: bool=False) -> bool:
    try:
        day = int(day)
    except ValueError:
        err = "Incorrect format for <Day>! Must be a <Number>"
        if show_messagebox: messagebox.showerror("Error", err)
        raise ValueError(err)

    try:
        month = int(month)
    except ValueError:
        err = "Incorrect format for <Month>! Must be a <Number>"
        if show_messagebox: messagebox.showerror("Error", err)
        raise ValueError(err)

    try:
        year = int(year)
    except ValueError:
        err = "Incorrect format for <Year>! Must be a <Number>"
        if show_messagebox: messagebox.showerror("Error", err)
        raise ValueError(err)

    try:
        if day > 31 or day < 1:
            raise ValueError("Day is out of range! [1 - 31]")
        if month > 12 or month < 1:
            raise ValueError("Month is out of range! [1 - 12]")
        if year > 9999 or year < 1:
            raise ValueError("Year is out of range! [1 - 9999]")
    except ValueError as ex:
        if show_messagebox: messagebox.showerror("Error", str(ex))
        return False

    Flair = [
        " I wonder what the future holds...",
        " Let's hope you live to see it!",
        " \nI hOpE NotHing BAd HapPenS oN ThIs ExAct DaY!"
    ]
    randomFlair = random.choice(Flair)

    if day <= days_in_month(year, month):
        if show_messagebox: messagebox.showinfo("Success! :^)", f"{day}/{month}/{year} Is Valid!" + randomFlair)
        return True
    else:
        if show_messagebox: messagebox.showwarning("Aw shucks :'(", f"{day}/{month}/{year} Is not valid...")

    return False

def get_random_date(iteration: int=0):
    for i in range(0, iteration):
        day = random.randrange(1, 50)
        month = random.randrange(1, 20)
        year = random.randrange(1, 10000)
    return day, month, year

def tkinter_set_text(entry: CTkEntry, text: str):
    entry.delete(0, "end")
    entry.insert(0, text)