import calendar
import random
from tkinter import messagebox
from customtkinter import CTkEntry

Config = {
    "window_title": "Date Time Checker",
    "window_size": "580x300",
    "logo_path": "logo.png",
    "logo_size": (250,70),
}

def days_in_month(year, month):
    return calendar.monthrange(year, month)[1]

def is_valid_date(year, month, day):
    try:
        day = int(day)
    except ValueError:
        messagebox.showerror("Error", "Incorrect format for <Day>! Must be a <Number>")
        return

    try:
        month = int(month)
    except ValueError:
        messagebox.showerror("Error", "Incorrect format for <Month>! Must be a <Number>")
        return

    try:
        year = int(year)
    except ValueError:
        messagebox.showerror("Error", "Incorrect format for <Year>! Must be a <Number>")
        return

    try:
        if day > 31 or day < 1:
            raise Exception("Day is out of range! [1 - 31]")
        if month > 12 or month < 1:
            raise Exception("Month is out of range! [1 - 12]")
        if year > 9999 or year < 1:
            raise Exception("Year is out of range! [1 - 9999]")
    except Exception as ex:
        messagebox.showerror("Error", str(ex))
        return

    Flair = [
        " I wonder what the future holds...",
        " Let's hope you live to see it!",
        " \nI hOpE NotHing BAd HapPenS oN ThIs ExAct DaY!"
    ]
    randomFlair = random.choice(Flair)

    if day <= days_in_month(year, month):
        messagebox.showinfo("Success! :^)", f"{day}/{month}/{year} Is Valid!" + randomFlair)
    else:
        messagebox.showwarning("Aw shucks :'(", f"{day}/{month}/{year} Is not valid...")

def get_random_date(iteration: int=0):
    for i in range(0, iteration):
        day = random.randrange(1, 50)
        month = random.randrange(1, 20)
        year = random.randrange(1, 10000)
    return day, month, year

def tkinter_set_text(entry: CTkEntry, text: str):
    entry.delete(0, "end")
    entry.insert(0, text)