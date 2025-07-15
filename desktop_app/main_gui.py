import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
import json
import os
import sys

# 🧠 Add backend to the path so 'src' can be imported
sys.path.append(os.path.abspath("../backend"))
from src.extractor import extract


def select_file():
    file_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if file_path:
        selected_file.set(file_path)
        file_label.config(text=os.path.basename(file_path))

def run_extraction():
    path = selected_file.get()
    format_selected = file_format.get()

    if not path or not os.path.exists(path):
        messagebox.showerror("Error", "Please select a valid PDF file.")
        return

    if format_selected not in ["patient_details", "prescription"]:
        messagebox.showerror("Error", "Please select a valid file format.")
        return

    try:
        result = extract(path, format_selected)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Extraction failed: {str(e)}")

# GUI Setup
app = tk.Tk()
app.title("MediScan - PDF Parser")
app.geometry("700x500")

# Title
tk.Label(app, text="MediScan Desktop App", font=("Helvetica", 16, "bold")).pack(pady=10)

# File selection
selected_file = tk.StringVar()
tk.Button(app, text="Choose PDF", command=select_file).pack()
file_label = tk.Label(app, text="No file selected", fg="gray")
file_label.pack(pady=5)

# File format selection
file_format = tk.StringVar()
tk.Label(app, text="Select File Format:").pack(pady=5)
format_menu = ttk.Combobox(app, textvariable=file_format, values=["patient_details", "prescription"])
format_menu.pack()
format_menu.set("patient_details")

# Run button
tk.Button(app, text="Run Extraction", command=run_extraction, bg="#4CAF50", fg="white").pack(pady=10)

# Output area
tk.Label(app, text="Extracted Output:").pack()
output_text = tk.Text(app, height=15, width=80)
output_text.pack(padx=10, pady=10)

# Run the app
app.mainloop()
