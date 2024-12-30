import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from PIL import Image
import os


# ---------------------------------------------------------------------------------------
# COLOR CONFIGURATION
# Adjust these color codes as desired.
# ---------------------------------------------------------------------------------------
WINDOW_BG_COLOR = "#edf2f4"       # Main window background color
LABEL_BG_COLOR = WINDOW_BG_COLOR  # Labels will match window background
LABEL_FG_COLOR = "#b01b07"        # Text (foreground) color of labels
BUTTON_BG_COLOR = "#8d99ae"       # Background color for buttons
BUTTON_BG_COLOR_HOVER = "#a1abbf" # Slightly lighter background when hovering
BUTTON_FG_COLOR = "#000000"       # Text (foreground) color for buttons

# ---------------------------------------------------------------------------------------
# FONT CONFIGURATION
# Adjust these tuples to control font families, sizes, and styles.
# ---------------------------------------------------------------------------------------
LABEL_FONT = ("Helvetica", 14)
BUTTON_FONT = ("Helvetica", 10, "bold")
DROPDOWN_FONT = ("Helvetica", 11)
# ---------------------------------------------------------------------------------------

def apply_hover_effects(button, normal_bg, hover_bg):
    """
    Bind <Enter> and <Leave> events to the button so it changes to hover_bg
    on mouse enter and reverts to normal_bg on mouse leave.
    """
    def on_enter(event):
        event.widget.configure(bg=hover_bg)
    def on_leave(event):
        event.widget.configure(bg=normal_bg)

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

class ImageConverterGUI:
    def __init__(self, master):
        """
        Initialize the GUI components and handle all possible issues
        that might arise (e.g., RGBA to JPEG conversion).
        """
        self.master = master
        self.master.title("Image Converter")
        
        # Set the icon (on Windows, this should appear in the window’s top-left corner)
        # self.master.iconbitmap("file_converter_img.ico")
        try:
            self.master.iconbitmap("file_converter_img.ico")
        except tk.TclError:
            print("Icon file not found. Using default icon.")

        
        # Increased the window size (width x height) for extra spacing
        self.master.geometry("300x200")
        self.master.resizable(False, False)

        # Apply window background color
        self.master.configure(bg=WINDOW_BG_COLOR)

        # Store the path of the selected file
        self.selected_file = None

        # 1. Label: Select an image
        self.select_label = tk.Label(
            self.master,
            text="Select an image to convert:",
            bg=LABEL_BG_COLOR,
            fg=LABEL_FG_COLOR,
            font=LABEL_FONT
        )
        self.select_label.pack(pady=5)

        # 2. Button: Select image
        self.select_button = tk.Button(
            self.master,
            text="Select Image",
            command=self.select_image,
            bg=BUTTON_BG_COLOR,
            fg=BUTTON_FG_COLOR,
            font=BUTTON_FONT,
            width=20  # Increased width
        )
        # Added extra padding below this button
        self.select_button.pack(pady=(2, 10))

        # 3. Dropdown label
        self.format_label = tk.Label(
            self.master,
            text="Choose output format:",
            bg=LABEL_BG_COLOR,
            fg=LABEL_FG_COLOR,
            font=LABEL_FONT
        )
        self.format_label.pack(pady=5)

        # 4. Dropdown (Combobox) for image formats
        self.available_formats = ["jpg", "png", "bmp", "gif", "tiff", "webp"]
        self.format_var = tk.StringVar(value=self.available_formats[0])
        self.format_dropdown = ttk.Combobox(
            self.master,
            textvariable=self.format_var,
            values=self.available_formats,
            state="readonly",
            font=DROPDOWN_FONT
        )
        self.format_dropdown.pack()

        # 5. Button: Convert and Save
        self.convert_button = tk.Button(
            self.master,
            text="Convert and Save",
            command=self.convert_and_save,
            bg=BUTTON_BG_COLOR,
            fg=BUTTON_FG_COLOR,
            font=BUTTON_FONT,
            width=20  # Matches the width of 'Select Image' button
        )
        self.convert_button.pack(pady=10)

        # Add the hover effect to both buttons
        self.add_hover_to_all_buttons()

    def add_hover_to_all_buttons(self):
        """
        Apply hover color changes to the 'Select Image' and 'Convert and Save' buttons.
        """
        apply_hover_effects(
            self.select_button,
            normal_bg=BUTTON_BG_COLOR,
            hover_bg=BUTTON_BG_COLOR_HOVER
        )
        apply_hover_effects(
            self.convert_button,
            normal_bg=BUTTON_BG_COLOR,
            hover_bg=BUTTON_BG_COLOR_HOVER
        )

    def select_image(self):
        """
        Let the user select an image file. Store the file path in self.selected_file.
        """
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[
                ("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif;*.tiff;*.webp"),
                ("All Files", "*.*")
            ]
        )
        if file_path:
            self.selected_file = file_path

    def convert_and_save(self):
        """
        Convert the selected image to the chosen format.
        Handle alpha channel issues for JPEG by converting RGBA to RGB.
        Then, let the user select a location to save it.
        """
        if not self.selected_file:
            messagebox.showerror("Error", "Please select an image first.")
            return

        chosen_format = self.format_var.get().lower()
        if chosen_format == "jpg":
            chosen_format = "jpeg"
        chosen_format_upper = chosen_format.upper()

        try:
            with Image.open(self.selected_file) as img:
                if chosen_format == "jpeg" and img.mode not in ["RGB", "L"]:
                    img = img.convert("RGB")

                file_path_to_save = filedialog.asksaveasfilename(
                    defaultextension=f".{chosen_format}",
                    filetypes=[
                        (f"{chosen_format_upper} Files", f"*.{chosen_format}"),
                        ("All Files", "*.*")
                    ],
                    title="Save Converted Image"
                )
                if not file_path_to_save:
                    return

                img.save(file_path_to_save, chosen_format_upper)

                messagebox.showinfo(
                    "Success", f"Image converted and saved as:\n{file_path_to_save}"
                )

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")

def main():
    root = tk.Tk()
    app = ImageConverterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
