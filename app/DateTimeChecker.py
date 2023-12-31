from tkinter import messagebox
import customtkinter
from PIL import Image
from app.DTCLib import Config, is_valid_date, get_random_date, tkinter_set_text
from itertools import cycle

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self, master=None):
        super().__init__(master)

        self.resizable(False, False)
        self.title(Config.get("window_title", None))
        self.geometry(Config.get("window_size", None))
        self.geometry(Config.get("window_position", None))
        
        ########### ROW 0
        self.logo_grid = customtkinter.CTkLabel(self, text=None)
        self.logo_grid.grid(row=0, column=0, padx=20, pady=(30, 30))
        
        label_logo_x, label_logo_y = 300, 30
        self.label_logo = customtkinter.CTkLabel(self, text="Date Time Checker", 
                                                 font=customtkinter.CTkFont(size=30, weight="bold"), 
                                                 text_color=("#1d4bcf", "#ff7d00"))
        self.label_logo.place(x=label_logo_x, y=label_logo_y)
        try:
            image0 = Image.open(Config.get("logo_path0", None))
            image1 = Image.open(Config.get("logo_path1", None))
            image2 = Image.open(Config.get("logo_path2", None))
            self.photos = cycle([
                customtkinter.CTkImage(image0, size=Config.get("logo_size", None)),
                customtkinter.CTkImage(image1, size=Config.get("logo_size", None)),
                customtkinter.CTkImage(image2, size=Config.get("logo_size", None))
            ])
            self.image = next(self.photos)
            self.image_label = customtkinter.CTkButton(self, image=self.image, text=None, command=self.change_logo_event,
                                                        fg_color="transparent", hover=None)
            self.image_label.place(x=10, y=10)
        except FileNotFoundError as e:
            messagebox.showwarning("Warning", f"{e}")

        ########### ROW 1 2
        self.lbl_day = customtkinter.CTkLabel(self, text="Day")
        self.lbl_day.grid(row=1, column=0)
        self.entry_day = customtkinter.CTkEntry(self, placeholder_text="dd")
        self.entry_day.grid(row=2, column=0, padx=30, pady=(0, 20))
        
        self.lbl_month = customtkinter.CTkLabel(self, text="Month")
        self.lbl_month.grid(row=1, column=1)
        self.entry_month = customtkinter.CTkEntry(self, placeholder_text="mm")
        self.entry_month.grid(row=2, column=1, padx=30, pady=(0, 20))

        self.lbl_year = customtkinter.CTkLabel(self, text="Year")
        self.lbl_year.grid(row=1, column=2)
        self.entry_year = customtkinter.CTkEntry(self, placeholder_text="yyyy")
        self.entry_year.grid(row=2, column=2, padx=30, pady=(0, 20))
        ########### ROW 3
        self.btn_clear_entries = customtkinter.CTkButton(self, text="Clear", command=self.clear_entries_event)
        self.btn_clear_entries.grid(row=3, column=0)

        self.btn_check_date = customtkinter.CTkButton(self, text="Check", fg_color="#451db5", command=self.check_date_event)
        self.btn_check_date.grid(row=3, column=2, padx=20, pady=10)
        self.bind('<Return>', lambda : self.check_date_event())
        ########### ROW 4 5
        self.lbl_appearance_mode = customtkinter.CTkLabel(self, text="Theme:")
        self.lbl_appearance_mode.grid(row=4, column=0)
        self.optmenu_appearance = customtkinter.CTkOptionMenu(self,
                                                        values=["System", "Light", "Dark"],
                                                        command=self.change_appearance_event)
        self.optmenu_appearance.grid(row=5, column=0)

        self.btn_rand_date_label = customtkinter.CTkLabel(self, text="Generate Random Date:")
        self.btn_rand_date_label.grid(row=4, column=1)
        self.btn_rand_date = customtkinter.CTkButton(self, text="Generate", command=self.rand_date_event)
        self.btn_rand_date.grid(row=5, column=1)
        ###########
        self.protocol('WM_DELETE_WINDOW', self.on_close)

    ########### EVENTS ###########
    def on_close(self):
        response = messagebox.askyesno('Confirm', 'Are you sure you want to exit?')
        if response: self.destroy()

    def clear_entries_event(self):
        self.entry_day.delete(0, "end")
        self.entry_month.delete(0, "end")
        self.entry_year.delete(0, "end")

    def check_date_event(self, show_messagebox=True):
        day = self.entry_day.get()
        month = self.entry_month.get()
        year = self.entry_year.get()
        return is_valid_date(year=year, month=month, day=day, show_messagebox=show_messagebox)

    def change_appearance_event(self, appearance_mode: str):
        customtkinter.set_appearance_mode(appearance_mode)

    def rand_date_event(self):
        day, month, year = get_random_date(10)
        tkinter_set_text(self.entry_year, year)
        tkinter_set_text(self.entry_month, month)
        tkinter_set_text(self.entry_day, day)

    def change_logo_event(self):
        self.image = next(self.photos)
        self.image_label.configure(image=self.image)

    def temp_btn_event(self):
        print("Button click! <:O")
