import customtkinter as ctk


class LoggerFrame(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)        
        self._textbox = ctk.CTkTextbox(self)
        self._textbox.pack(fill="both", expand=True)

    def log(self, message: str, next_line: bool = True):
        if next_line:
            msg = message.strip() + "\n"
        else:
            msg = message.strip()
        self._textbox.configure(state="normal")
        self._textbox.insert("end", msg)
        self._textbox.configure(state="disabled")


class EntranceFrame(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.name_var = ctk.StringVar(value="")

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(expand=True, fill="both")

        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.pack(expand=True, fill="both")

        self.name_label = ctk.CTkLabel(self.top_frame, text="Enter your name")
        self.name_label.pack()

        self.name_entry = ctk.CTkEntry(self.top_frame, textvariable=self.name_var)
        self.name_entry.pack()

        self.enter_btn = ctk.CTkButton(self.bottom_frame)
        self.enter_btn.pack()